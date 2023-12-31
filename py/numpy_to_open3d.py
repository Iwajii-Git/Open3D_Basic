import open3d as o3d
import numpy as np

#点群の作成
pt = np.ones((100,3),dtype=np.float64)
cl = np.ones((100,3),dtype=np.float64)
#pt，clのデータ型を見る
print(f"ptのタイプは{type(pt)}，点の数は{len(pt)}")
print(f"clのタイプは{type(cl)}，点の数は{len(cl)}")


#numpy→open3d変換
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(pt)
pcd.colors = o3d.utility.Vector3dVector(cl)

#pcdのデータ型を見る
print(f"pcdのタイプは{type(pcd)}，点の数は{pcd}")


