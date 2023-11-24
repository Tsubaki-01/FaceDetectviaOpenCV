from save_face import save_face_through_capture
from trainer import train

if __name__ == '__main__':
    save_face_through_capture('test2')  # 写名字

    data_path = '../faces_saved'
    save_path = '../trainer'
    train(data_path, save_path)
