import open3d as o3d
import numpy as np

#点群の読み込み
pcd = o3d.io.read_point_cloud("cow_data.ply")
#ダウンサンプリング
pcd = pcd.voxel_down_sample(voxel_size=0.01)
#点群の表示
o3d.visualization.draw_geometries([pcd])

#切り取る部分の選択
select = o3d.geometry.OrientedBoundingBox(
    np.array([[-1],[-1],[-1]]),
    np.array([[0.5,0.1,-0.1],[-0.1,1,0.1],[1,-0.1,0.5]]),
    np.array([[1],[5],[5]]),
)

#点群の切り取り
cropped_pcd = pcd.crop(select)

#切り取った点群の表示
o3d.visualization.draw_geometries([cropped_pcd])