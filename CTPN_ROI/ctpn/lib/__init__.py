import sys
sys.path.append('./ctpn/lib') # 'E:\\PyProjects\\Codes\\RMB_TechDing\\FTPN_ROI\\ctpn\\lib'
from .networks.factory import get_network
from .fast_rcnn.config import cfg,cfg_from_file
from .fast_rcnn.test import test_ctpn
from .utils.timer import Timer
from .text_connector.detectors import TextDetector
from .text_connector.text_connect_cfg import Config as TextLineCfg