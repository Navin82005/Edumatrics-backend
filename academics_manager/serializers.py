import openpyxl


def timetable_extractor(_file: openpyxl) -> list:
    sheet = _file.active
    raw_sheet_data = [list(i) for i in sheet.iter_rows(values_only=True)]

    # print("raw_sheet_data", raw_sheet_data)

    subjects = []

    def extract_timetable(raw_sheet_data: list) -> dict:
        timetable = {}
        _subject = {}
        timetable["year"] = (raw_sheet_data[0][0].split(":")[1]).strip()
        _subject["year"] = timetable["year"]
        _subject["subjects"] = []
        timetable["department"] = (raw_sheet_data[0][1].split(":")[1]).strip()
        timetable["section"] = (raw_sheet_data[0][2].split(":")[1]).strip()
        timetable["semester"] = (raw_sheet_data[0][3].split(":")[1]).strip()
        timetable["class room"] = (raw_sheet_data[0][4].split(":")[1]).strip()

        raw_sheet_data = raw_sheet_data[1:]

        timings = raw_sheet_data[0]
        day_timetable = {}
        k = 1

        original_days = {}

        temp_day = {}

        for i in raw_sheet_data[1:]:
            day_timetable[i[0]] = {}
            priv_period = ""
            k = 1
            is_none = False
            new_time = ""
            priv_time = timings[k]
            cur_time = timings[k]
            subject_state = True
            original_days[i[0]] = {}
            for j in i[1:]:
                for dicts in subjects:
                    subject_state = dicts["year"] != timetable["year"]
                if (
                    subject_state
                    and str(j).lower() not in _subject["subjects"]
                    and j is not None
                ):
                    _subject["subjects"].append(str(j).lower())
                cur_time = timings[k]
                if str(j).lower() != "none" and str(j).lower() != "lunch break":
                    is_none = False
                    priv_period = j
                    priv_time = timings[k]
                else:
                    is_none = True
                if is_none:
                    new_time = (
                        priv_time.split(" - ")[0] + " - " + cur_time.split(" - ")[1]
                    )
                    temp_day[priv_period] = new_time
                else:
                    temp_day = {}
                    pass
                try:
                    if temp_day != {} and str(i[k + 1]).lower() != "none":
                        original_days[i[0]][temp_day[priv_period]] = priv_period
                    elif str(i[k + 1]).lower() != "none":
                        original_days[i[0]][cur_time] = str(j)
                except IndexError:
                    if str(i[k]).lower() != "none":
                        original_days[i[0]][cur_time] = str(j)
                k += 1

        for i in temp_day:
            original_days["Saturday"][temp_day[i]] = i

        timetable["timetable"] = original_days
        if not subject_state:
            return timetable, None
        return timetable, _subject

    data_list = []
    k = 0
    for i in range(len(raw_sheet_data)):
        if set(raw_sheet_data[i]) == {None}:
            temp_data = extract_timetable(raw_sheet_data[k:i])
            data_list += [temp_data[0]]
            if temp_data[1] is not None:
                subjects += [temp_data[1]]
            k = i + 1

    temp_data = extract_timetable(raw_sheet_data[k:])
    data_list += [temp_data[0]]
    if temp_data[1] is not None:
        subjects += [temp_data[1]]

    return data_list, subjects


if __name__ == "__main__":
    fh = openpyxl.open("timetable.xlsx", data_only=True)

    print(timetable_extractor(fh))
