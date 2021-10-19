import time
c = time.time()

s_a = 60.
m_a = 60.
h_a = 24.
d_a = 365.
d_l = 366.

y_a= d_a*h_a*m_a*s_a # standard years in seconds
y_l= d_a*h_a*m_a*s_a # leap years in seconds

#number of seconds since 1970
epoch = y_a #1 Jan 1971
epoch = 2*y_a # 1 Jan 1972
epoch = 2*y_a + y_l # 1 Jan 1973
epoch = 3*y_a + y_l # 1 Jan 1974
