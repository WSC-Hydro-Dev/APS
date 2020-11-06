def getTimeSeriesData(token, timeseriesID, fromDate, toDate):
    '''
    Get the corrected time series data from AQ NG
    :param timeseriesID: ID of specific timeseries (station@time.series)
    :param fromDate: start date of timeseries
    :param toDate: End date of timeseries
    :return: Timeseries data in raw json
    '''
    command = "http://wsc.aquaticinformatics.net/AQUARIUS/Publish/v2/GetTimeSeriesCorrectedData"
    params = {"token": token,
              "TimeSeriesUniqueId": timeseriesID,
              "QueryFrom": str(fromDate)[:10],
              "QueryTo": str(toDate)[:10]}

    r = requests.get(command, params)
    json_timeseries = r.json()

    return json_timeseries