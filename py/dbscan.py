import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt

#点群の読み込み
pcd = o3d.io.read_point_cloud("cow_data.ply")
#ダウンサンプリング
pcd = pcd.voxel_down_sample(voxel_size=0.01)
#点群の表示
o3d.visualization.draw_geometries([pcd])

def Dbscan():
    #DBSCAN
    db = pcd.cluster_dbscan(eps=0.1, min_points=270)
    #DBSCANで得たラベル情報をnumpyへ変換
    labels = np.array(db)
    #labelsの中での最大値を計算
    max_label = labels.max()

    #クラスタリングされた物体の個数の表示(最大値+1==クラスタリングされた数)
    print(f"point cloud has {max_label + 1} clusters")

    #物体ごとに色分け
    seg = plt.get_cmap("tab20")(labels / max(max_label,1))
    #ラベルが0より小さい値，すなわちノイズ値は0を代入して透明化
    seg[labels < 0] = 0

    #セグメンテーションの可視化
    pcd_seg =o3d.geometry.PointCloud()
    pcd_seg.points = o3d.utility.Vector3dVector(pcd.points)
    pcd_seg.colors = o3d.utility.Vector3dVector(seg[:, :3])
    o3d.visualization.draw_geometries([pcd_seg])

    #labelsを戻り値に設定
    return labels

def Devide(labels, points, colors, d):#セグメンテーションを行う
    p = 0
    #選択されたラベルの物体の点群数がいくつなのか調べている
    count = np.count_nonzero(labels == d)
    print(f"{d+1}番目の点群数:{count}")
    
    #点群を代入する配列を宣言しておく
    pcd_pt = np.zeros((count, 3), dtype=np.float32)
    pcd_cl = np.zeros((count, 3), dtype=np.float32)

    for k in range(len(labels)):#ここでラベルごとに点群を分けている
        if (labels[k] == d):
            pcd_pt[p] = points[k]
            pcd_cl[p] = colors[k]
            p = p + 1

    #点群を統合している
    pcd_dv =o3d.geometry.PointCloud()
    pcd_dv.points = o3d.utility.Vector3dVector(pcd_pt)
    pcd_dv.colors = o3d.utility.Vector3dVector(pcd_cl)

    #分類された点群を戻り値に設定
    return pcd_dv


################## main ########################
#まずDBSCANしてクラスタリングされたラベルを代入
labels = Dbscan()
#for文を回してラベルごとに点群を抽出
for d in range(0,labels.max()+1):
    #DBSCANして得たラベルの値を基に点群を分類
    pcd_dv = Devide(labels,pcd.points,pcd.colors,d)
    #分類した点群の表示
    o3d.visualization.draw_geometries([pcd_dv])
    #分類した点群の保存
    #o3d.io.write_point_cloud(f"DBSCAN{d+1}.ply", pcd_dv)

