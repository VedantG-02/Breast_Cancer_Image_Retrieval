import os

def read_data():
    ls=[]
#     path=os.path.join(os.getcwd(),'..','BreaKHis_v1','histology_slides','breast','benign','SOB','adenosis','40X')
    path = os.path.join(os.getcwd(),'BreaKHis_v1','histology_slides','breast','malignant','SOB')
    i=5
    for file2 in os.listdir(path):
        i+=1
        for file3 in os.listdir(os.path.join(path,file2)):
            for file4 in os.listdir(os.path.join(path,file2,file3,'400X')):
                os.replace(os.path.join(path,file2,file3,'400X',file4),os.path.join(os.getcwd(),'BreaKHis_v1','Dataset_400X','Malignant',str(i-1),file4))
    return 'done'
if __name__=='__main__':
    print(read_data())