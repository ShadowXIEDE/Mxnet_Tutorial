import randomimport numpy as npimport pandas as pdimport seaborn as snsimport matplotlib.pyplot as pltfrom tqdm import *#I refer to the k-means code in the book, "TensorFlow First Steps."def K_means_Algorithm_numpy(epoch=100,point_numbers=2000,centroid_numbers=5):    dataset=[]    centroid=[]    # data generation    for i in range(point_numbers):        if random.random() > 0.5:            dataset.append([np.random.normal(loc=0,scale=0.9),np.random.normal(loc=0,scale=0.9)])        else:            dataset.append([np.random.normal(loc=3,scale=0.5),np.random.normal(loc=0,scale=0.9)])    df = pd.DataFrame({"x": [d[0] for d in dataset] , "y": [d[1] for d in dataset]})    sns.lmplot("x","y" , data=df , fit_reg=False , size=10)    plt.savefig("K means Algorithm init using numpy.png")    # 1-step    random.shuffle(dataset)    for i in range(centroid_numbers):        centroid.append(random.choice(dataset))    # data assignment , updating new center values    for i in tqdm(range(epoch)):        # 2-step        diff = np.subtract(np.expand_dims(dataset,axis=0),np.expand_dims(centroid,axis=1))        sqr = np.square(diff)        distance = np.sum(sqr,axis=2)        clustering = np.argmin(distance,axis=0)        '''        for j in range(centroid_numbers):            centroid[j][:]=np.mean(np.take(dataset,np.reshape(np.where(np.equal(clustering,j)), (-1,)),axis=0),axis=0)'''        # 3-step        centroid[:] = [np.mean(np.take(dataset, np.reshape(np.where(np.equal(clustering, cn)),(-1,)), axis=0),axis=0) for cn in range(centroid_numbers)]        print("epoch : {}".format(i+1))    for i in range(centroid_numbers):        print("{}_center : Final center_value : {}" . format(i+1,centroid[i]))    #4 show result    data = {"x": [], "y": [] , "cluster" : []}    for i in range(len(clustering)):        data["x"].append(dataset[i][0])        data["y"].append(dataset[i][1])        data["cluster"].append(clustering[i])    df = pd.DataFrame(data)    sns.lmplot("x", "y", data=df, fit_reg=False, size=10 , hue="cluster")    plt.savefig("K means Algorithm completed using numpy.png")    plt.show()if __name__ == "__main__":    K_means_Algorithm_numpy(epoch=100, centroid_numbers=5, point_numbers=2000)else:    print("numpy kmeans Imported")