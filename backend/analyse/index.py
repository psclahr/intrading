from backend.analyse.bootstrap import bootstrap

def start():
    bootstrap()

    # visualizeData(data)

    # filteredData = list(filter(lambda day: day['open'] is not None , data))

    # candleStickRecognizer = Recognizer(filteredData)

    # candleSticks = {}

    # for index, day in enumerate(filteredData):
      #   result = candleStickRecognizer.whichCandleStick(index)

        # if result is not None:
          #   name = result['name']
            # index = result['index']

            # if name in candleSticks:
              #   candleSticks[name].append(index)
            # else:
              #   candleSticks[name] = [index]

    # predicter = Predicter(filteredData)

    # predictions = {}

    # for candleStickName in candleSticks:
      #   prediction = predicter.predict(candleSticks[candleStickName])

        # predictions[candleStickName] = prediction

    # return predictions
