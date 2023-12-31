import open3d as o3d
import numpy as np
import copy

#点群の読み込み
pcd = o3d.io.read_point_cloud("cow_data.ply")
#ダウンサンプリング
pcd = pcd.voxel_down_sample(voxel_size=0.01)
#xyz軸の作成(赤:X軸，緑:Y軸，青:Z軸)
mesh = o3d.geometry.TriangleMesh.create_coordinate_frame()
#点群の表示
o3d.visualization.draw_geometries([pcd,mesh])
#deep_copyしている
pcd_t = copy.deepcopy(pcd)
pcd_r = copy.deepcopy(pcd)


#####################平行移動#########################
#座標(1,1,1)に平行移動
pcd_t.translate([1,1,1])

#点群の表示
o3d.visualization.draw_geometries([pcd,pcd_t,mesh])
####################ここまで##########################

####################回転##############################
#どれだけ回転させるか(弧度法)
R = mesh.get_rotation_matrix_from_xyz((np.pi / 2, 0, 0))
#点群の回転
pcd_r.rotate(R, center=(0,0,0))

#点群の表示
o3d.visualization.draw_geometries([pcd,pcd_r,mesh])
####################ここまで##########################