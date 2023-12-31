import open3d as o3d

#点群の読み込み
ptCloud = o3d.io.read_point_cloud("cow_data.ply")

#ダウンサンプリング
uds = ptCloud.uniform_down_sample(every_k_points=10)

#ダウンサンプリングしたあとの点群を描画
o3d.visualization.draw_geometries([uds])
