import open3d as o3d

#点群の読み込み
ptCloud = o3d.io.read_point_cloud("cow_data.ply")

#点群の描画
o3d.visualization.draw_geometries([ptCloud])

#点群が何点あるか表示
print(ptCloud)