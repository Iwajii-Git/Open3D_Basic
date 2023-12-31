import open3d as o3d
import numpy as np

#点群の読み込み
pcd = o3d.io.read_point_cloud("cow_data.ply")
#ダウンサンプリング
pcd = pcd.voxel_down_sample(voxel_size=0.01)
#点群の表示
o3d.visualization.draw_geometries([pcd])

#点群の選択範囲(平面)を決めている．今回はxz平面
corners = np.array([
    [0.7, 0, 0.1],
    [-0.7, 0, -1.5],
    [-0.5, 0, 0.1],
    [0.5, 0, -1.5],
], dtype=np.float64)

#インスタンス化
vol = o3d.visualization.SelectionPolygonVolume()
#今回はY軸方向に伸ばす
vol.orthogonal_axis = "Y"
#上限
vol.axis_max = 50
#下限
vol.axis_min = -10

#インスタンス化したvolの中にどの平面を伸ばすかを示すbounding_polygon配列の中に代入している
vol.bounding_polygon = o3d.utility.Vector3dVector(corners)

#点群の切り取り
cropped_pcd = vol.crop_point_cloud(pcd)

#切り取った点群の表示
o3d.visualization.draw_geometries([cropped_pcd])