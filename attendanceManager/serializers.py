from datetime import datetime

def get_period_cell(lh):
    cell = '1'
    _time1 = datetime.strptime("10:50", "%H:%M").time()
    _now_time = datetime.now().time()
    _time2 = datetime.strptime("11:50", "%H:%M").time()
    
    print(_time1 < _now_time, _now_time < _time2)


    return cell
