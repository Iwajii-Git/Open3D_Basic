import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt

#点群の読み込み
pcd = o3d.io.read_point_cloud("cow_data.ply")

#ダウンサンプリング
pcd = pcd.voxel_down_sample(voxel_size=0.01)

#点群の描画
o3d.visualization.draw_geometries([pcd])

############################メッシュの計算##############################
#法線推定
pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))

#面に対する法線方向の一貫性を保つ
pcd.orient_normals_consistent_tangent_plane(100)

#メッシュの計算
mesh, densities = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcd, depth=9)

#点群の表示
o3d.visualization.draw_geometries([mesh])
################################ここまで##########################

################################点群密度の可視化##########################
#densitiesをnumpy配列に変換
densities = np.asarray(densities)

#matplotlibで密度の値によって色を付けている
density_colors = plt.get_cmap('plasma')((densities - densities.min()) / (densities.max() - densities.min()))

#必要な値だけを取り出す
density_colors = density_colors[:, :3]

#インスタンス化
density_mesh = o3d.geometry.TriangleMesh()

#色情報以外のメッシュの値を代入
density_mesh.vertices = mesh.vertices
density_mesh.triangles = mesh.triangles
density_mesh.triangle_normals = mesh.triangle_normals

#色情報のみ33行目で作成したメッシュを用いている
density_mesh.vertex_colors = o3d.utility.Vector3dVector(density_colors)

#メッシュの可視化
o3d.visualization.draw_geometries([density_mesh])
################################ここまで##########################

################################点群密度の低い箇所の削除##########################
#削除する部分を選定している
vertices_to_remove = densities < np.quantile(densities, 0.01)

#密度の低い箇所を削除している
mesh.remove_vertices_by_mask(vertices_to_remove)

#メッシュの可視化
o3d.visualization.draw_geometries([mesh])
################################ここまで##########################