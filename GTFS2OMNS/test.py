# Note:
# 1. Need dependency autoinstall
# 2. GDAL

import os
os.environ['PATH']
import gtfs2gmns as gg

gtfs_path = "H:\\ChromeDownload\\gtfscota"
gmns_path = "H:\\ChromeDownload\\gtfscota\\output"

node_transit,link_transit = gg.Convert_GTFS(gtfs_path,gmns_path)