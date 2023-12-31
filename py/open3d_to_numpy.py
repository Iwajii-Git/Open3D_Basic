import open3d as o3d
import numpy as np

#点群の読み込み
pcd = o3d.io.read_point_cloud("cow_data.ply")
#pcdのデータ型を見る
print(f"pcdのタイプは{type(pcd)}，点の数は{pcd}")

#open3d→numpy変換
pt = np.asarray(pcd.points)
cl = np.asarray(pcd.colors)
#pt，clのデータ型を見る
print(f"ptのタイプは{type(pt)}，点の数は{len(pt)}")
print(f"clのタイプは{type(cl)}，点の数は{len(cl)}")
