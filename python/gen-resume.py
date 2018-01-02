# -*- coding: UTF-8 -*-
import pystache
from resume_master import ResumeMaster

renderer = pystache.Renderer()
master = ResumeMaster()

print renderer.render(master).encode('utf-8')
