from pickle import load
from facenet_pytorch import MTCNN, InceptionResnetV1
import torch
from torchvision import datasets
from torch.utils.data import DataLoader
from PIL import Image
import os
import cv2
import numpy as np
def detectFace(img, path = True):
    '''
    Hàm phát hiện khuôn mặt từ img và trả về 1 torch.Size([3, 240, 240])

    Param: nếu path == True thì img là Relavetive path của ảnh (dùng để train), ngược lại thì img là ảnh dùng để chấm công
    Return: torch.Size([3, 240, 240])
    '''
    detector = MTCNN(image_size=240, margin=0, min_face_size=20) 
    face, prob = detector(img, return_prob = True)
    # plt.imshow(face.permute(1,2,0))
    return face, prob
    
# Các hàm hỗ trợ load ảnh và lưu data
def getIDList(path):
    '''
    Input: path Images folder
    Output: ID list

    Hàm trả về list các ID của User
    '''
    return os.listdir(path)


def collate_fn(x):
    return x[0]

def extractingFolder():
    dataset = datasets.ImageFolder('Img\\User_Image')
    index_to_class = os.listdir("Img\\User_Image")
    loader = DataLoader(dataset, collate_fn=collate_fn)
    
    #khởi tạo MTCNN để phát hiện khuôn mặt
    mtcnn = MTCNN(image_size=240, margin=0, min_face_size=20)
    #khởi tạo resnet để nhúng khuôn mặt thành vector
    resnet = InceptionResnetV1(pretrained='vggface2').eval()

    name_list = [] #danh sách tên của những khuôn mặt
    embedding_list = [] #danh sách các ma trận khuôn mặt đã được nhúng ở bước Resnet

    for img, idx in loader:
        face, prob = mtcnn(img, return_prob=True)
        #nếu khuôn mặt được xác định 
        #và đánh giá tỉ lệ % độ chính xác mà module detect được
        if face is not None and prob>0.95:
            #chuyển khuôn mặt đã được cắt sang resnet model để nhúng thành vector
            emb = resnet(face.unsqueeze(0))
            #chèn kết quả vào danh sách embedding_list
            embedding_list.append(emb.detach())
            #tên của người đó cũng được thêm vào danh sách 
            name_list.append(index_to_class[idx])

    data = [embedding_list, name_list]
    torch.save(data, "data.pt")
    
def load_resnet():
    return InceptionResnetV1(pretrained='vggface2').eval()

def load_saved_data():
    return torch.load('data.pt')

def face_match(img_path, resnet, saved_data, path = True):
    #gọi hàm xác định khuôn mặt
    if path == True:
        img = Image.open(img_path)
    else:
        img = img_path
    face, prob = detectFace(img)
    if face is not None and prob>0.90:
    #trả về một ảnh cắt khuôn mặt và tỉ lệ % độ chính xác
        emb = resnet(face.unsqueeze(0)).detach()
        #gradient false
        embedding_list = saved_data[0]
        name_list = saved_data[1]
        dist_list = [] #danh sách khoảng cách của test và vector train

    for idx, emb_db in enumerate(embedding_list):
        #tính khoảng cách giữa emb test với emb database trong file pt
        dist = torch.dist(emb, emb_db).item()
        dist_list.append(dist)
    idx_min = dist_list.index(min(dist_list))
    return (name_list[idx_min], min(dist_list)) if min(dist_list) <= 0.9 else -1

'''extractingFolder()

saved_data = load_saved_data()
resnet = load_resnet()
result = face_match("Img\data_test\MV5BMjAwMjk3NDUzN15BMl5BanBnXkFtZTcwNjI4MTY0NA@@._V1_UY1200_CR85,0,630,1200_AL_.jpg", resnet, saved_data)

if result != -1:
    print('Face matched with: ', result[0], 'with distance: ', result[1])
else:
    print("No exist")

#temp = load_saved_data()
#print(temp[0][2].shape)
print(type(saved_data))'''


def testAccuracy():
    data_path = "F:\Projects\HeThongChamCong\Img\data_test"
    images = os.listdir(data_path)
    y_test = [1, 1, 5, 1, 1, 2, 4, 4, 3, 3, 5, 5, 5, 5, 5, 5, 5, 1, 1, 4]
    saved_data = load_saved_data()
    resnet = load_resnet()
    y_pre = []
    count = 0
    for image in images:
        path = data_path + "/" + image
        temp = face_match(path, resnet, saved_data)
        if temp == -1:
            y_pre.append(-1)
            print(path)
        else:
            y_pre.append(temp[0])
    
    for i in range(len(y_test)):
        if y_test[i] == int(y_pre[i]):
            count+=1
    print(y_pre)
    print((count/20)*100)

'''img = cv2.imread("Img\data_test\download.jpg")
print(type(img))
print(img.shape)
print(face_match(img, resnet=load_resnet(), saved_data=load_saved_data(), path=False))'''
#extractingFolder()