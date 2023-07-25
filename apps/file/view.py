from flask import Blueprint,render_template,request,url_for,redirect
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from exts import db
from apps.file.model import File

plt.rcParams["font.sans-serif"]=["SimHei"] 
plt.rcParams["axes.unicode_minus"]=False

file_bp = Blueprint('file',__name__,url_prefix='/file')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in {'xls','xlsx'}
#判断文件名后缀
@file_bp.route('/')
def index():
    return render_template('file/try-boot.html')
@file_bp.route('/upload',methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            file.save('uploads/' + file.filename)
            path = f'uploads/{file.filename}'
            pol = pd.read_excel(path)
            pd.options.display.float_format = '{:.2f}'.format
#相关性分析
            corr_matrix = pol.iloc[:,1:].corr()
            mpl.rcParams['font.size'] = 8
            figure(figsize=(20, 20), dpi=300)
            sns.heatmap(corr_matrix , annot = True , cmap='rainbow',fmt='.2f',annot_kws={'fontsize':25},square=False)
            plt.title('Heatmap',fontsize=50)
            plt.xticks(fontsize=20,rotation=90)
            plt.yticks(fontsize=20,rotation=360)
            path_name = 'static/images/'
            file_name = 'heatmap2.jpg'
            file_path = path_name + file_name
            plt.savefig(file_path)
#主成分分析
            pca = PCA(n_components=5)
            data_pca = pca.fit_transform(pol.iloc[:,1:-1])
            mpl.rcParams['font.size'] = 7
            figure(figsize=(8,6),dpi=300)
            plt.scatter(data_pca[:,0],data_pca[:,1],s = data_pca[:,2]*250,alpha=0.8)
            plt.xlabel('PC1',fontsize=14)
            plt.xticks(fontsize=14)
            plt.ylabel('PC2',fontsize=14)
            plt.yticks(fontsize=14)
            plt.title('PCA Bubbles',fontsize=18)
            path_name = 'static/images/'
            file_name = 'bubbles.jpg'
            file_path = path_name + file_name
            plt.savefig(file_path)
#聚类分析
            data = pol.iloc[:,1:].values
            scaler = StandardScaler()
            features_scaled = scaler.fit_transform(data)
            kmeans = KMeans(n_clusters=4, random_state=42)
            kmeans.fit(features_scaled)
            labels = kmeans.labels_ # 获取聚类标签
            mpl.rcParams['font.size'] = 7
            figure(figsize=(8,6), dpi=300)
            plt.scatter(features_scaled[:,0], features_scaled[:,1], c=labels)
            plt.xlabel('Feature 1',fontsize=14)
            plt.xticks(fontsize=14)
            plt.ylabel('Feature 2',fontsize=14)
            plt.yticks(fontsize=14)
            plt.title('Kmeans Cluster',fontsize=18)
            path_name = 'static/images/'
            file_name = 'kmeans.jpg'
            file_path = path_name + file_name
            plt.savefig(file_path)

            return render_template('file/show.html',pol = pol.head().to_html())
        else:
            return '文件或文件扩展名不合法!'
    return render_template('file/upload.html')