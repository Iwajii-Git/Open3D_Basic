import open3d as o3d

#点群の読み込み
pcd = o3d.io.read_point_cloud("cow_data.ply")
#ダウンサンプリング
pcd = pcd.voxel_down_sample(voxel_size=0.01)
#点群の表示
o3d.visualization.draw_geometries([pcd])


#AlphaShapeの実行
mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_alpha_shape(pcd, alpha=0.05)
#頂点の法線を計算
mesh.compute_vertex_normals()

#作成したメッシュの表示
o3d.visualization.draw_geometries([mesh], mesh_show_back_face=True)

