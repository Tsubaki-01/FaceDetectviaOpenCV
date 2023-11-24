import json
import os


# -1 empty file
# -2 none found

class FaceDicOperator:

    @staticmethod
    def search_face_in_the_dic_by_key(key1):
        #   face dictionary is empty
        if os.path.getsize('../faces_saved/face_dictionary.json') == 0:
            return -1
        #   search the face dictionary
        with open('../faces_saved/face_dictionary.json', 'r') as face_dic_file:
            face_dic = json.load(face_dic_file)
            return face_dic.get(key1, -2)
            # for key, value in face_dic.items():
            #     if key1 == key:
            #         return value
            #     else:
            #         return -2

    @staticmethod
    def search_face_in_the_dic_by_value(value1):
        #   face dictionary is empty
        if os.path.getsize('../faces_saved/face_dictionary.json') == 0:
            return -1
        #   search the face dictionary
        with open('../faces_saved/face_dictionary.json', 'r') as face_dic_file:
            face_dic = json.load(face_dic_file)
            for key, value in face_dic.items():
                if value1 == value:
                    return key
            return -2

    @staticmethod
    def add_face_to_the_dic(string) -> bool:
        #   face dictionary is empty
        if os.path.getsize('../faces_saved/face_dictionary.json') == 0:
            new_key = 0
            face_dic = {}
        #   read the face dictionary
        else:
            with open('../faces_saved/face_dictionary.json', 'r') as face_dic_file:
                face_dic = json.load(face_dic_file)
                new_key = int(max(face_dic.keys())) + 1
        #   add
        with open('../faces_saved/face_dictionary.json', 'w') as face_dic_file:
            face_dic[new_key] = string
            json.dump(face_dic, face_dic_file)
        return new_key in face_dic


if __name__ == '__main__':
    face_dic_operator = FaceDicOperator()
    # face_dic_operator.add_face_to_the_dic('strauss')
    print(f'{face_dic_operator.search_face_in_the_dic_by_key("0")}')
    print(f'{face_dic_operator.search_face_in_the_dic_by_value("test2")}')
