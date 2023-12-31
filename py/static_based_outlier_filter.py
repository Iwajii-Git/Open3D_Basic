import open3d as o3d

#点群の読み込み
ptCloud = o3d.io.read_point_cloud("cow_data.ply")
vds = ptCloud.voxel_down_sample(voxel_size=0.01)

#この関数は推定したノイズに色を付けている
def display_inlier_outlier(cloud, ind):
    #ノイズと判断されなかった点群の番号を変数に代入している
    inlier_cloud = cloud.select_by_index(ind)
    #ノイズと判断された点群の番号を変数に代入している
    outlier_cloud = cloud.select_by_index(ind, invert=True)
    #ノイズと判断された点群に赤色をつけている
    outlier_cloud.paint_uniform_color([1, 0, 0])
    #ノイズと判断されなかった点群に灰色をつけている
    inlier_cloud.paint_uniform_color([0.8, 0.8, 0.8])
    #点群の描画
    o3d.visualization.draw_geometries([inlier_cloud, outlier_cloud])
                                      
#点群のノイズを判断している．clはノイズを取り除いた点群データ，indはそのノイズと判断されなかった点群の番号を代入されている．
cl, ind = vds.remove_statistical_outlier(nb_neighbors=20, std_ratio=2.0)
#関数呼び出し
display_inlier_outlier(vds, ind)