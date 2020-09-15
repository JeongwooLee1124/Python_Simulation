from Simulation import Simulation
from SimulationAnalysis import SimulationAnalysis
import numpy as np
import math
import pandas as pd

simFig2 = Simulation(100)
simFig2.setup("Figure2")
simFig2.run(500)
# sa2 �� ��� Ȯ�����ؼ� ����
sa2 = SimulationAnalysis(simFig2)
sa2.customerSummary
# �Ʒ� ��ɾ� �����ϸ� �����ϱ� ���� ���� ����
sa2.analyzeSystemPerformance()
simFig3 = Simulation(100)
simFig3.setup("Figure3")
simFig3.run(500)
# simFig3�� �����ϰ� ���� ������ simFig3 �� ��� ���ϱ� ���ؼ� �Ʒ� ����
# �Ʒ� �����ϸ� ������ ����� simFig2 - simFig3 ��� ��
# ���� ���� Page 16�� �����ؼ� ���� ���� �� ����
# ���⼭ ���� ���� �������� ���� simFig3�� simFig3.setup("Figure3") ������ �ϸ�
# simFig3.run(500)���� �ڵ����� ������.
# �⺻������ simFig3.run(500) ���� �ùķ��̼��� ������ ���� �Ʒ��� ���� �����ϴ� ����
# ���� �����.
sa2.comparePerformance(simFig3)

# ���� simFig3�� ����� �˰� ������, SimulationAnalysis�� �ϳ� �� ���� ���� ������.
sa3 = SimulationAnalysis(simFig3)
sa3.analyzeSystemPerformance()

