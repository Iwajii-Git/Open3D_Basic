import open3d as o3d

#点群の読み込み
ptCloud = o3d.io.read_point_cloud("cow_data.ply")

#ダウンサンプリング
vds = ptCloud.voxel_down_sample(voxel_size=0.05)

#ダウンサンプリングしたあとの点群を描画
o3d.visualization.draw_geometries([vds])