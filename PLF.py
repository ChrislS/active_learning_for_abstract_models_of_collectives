# Author: Christoph Lassner
import numpy as np

class PLF(object):
    def __init__(self):
        self.data_points = None

    def fit(self, X, Y):
        assert X.shape == Y.shape
        assert X.shape[0] > 1
        assert X.ndim == 1
        assert Y.ndim == 1
        assert np.unique(X).shape == X.shape, 'PLF only supports one point '+\
               'for each X position. Shapes: %s, %s' % \
               (str(np.unique(X).shape), str(X.shape))
        sortperm = np.argsort(X.flat)
        self.X = X[sortperm]
        self.Y = Y[sortperm]

    def predict(self, data):
        predictions = np.empty(data.shape)
        for pointidx, point in enumerate(data):
            smallerind = 0
            greaterind = 1
            if point <= self.X[0]:
                pass
            elif point >= self.X[-1]:
                smallerind = self.X.shape[0]-2
                greaterind = self.X.shape[0]-1
            else:
                # There is a greater and smaller element.
                smallerind = np.argmin(self.X <= point)-1
                greaterind = np.argmax(self.X > point)
            if not greaterind == smallerind+1:
                print smallerind, greaterind, point, self.X[smallerind:greaterind+1]
            assert greaterind == smallerind+1, '%d, %d' % (smallerind, greaterind)
            xsmaller = self.X[smallerind]
            ysmaller = self.Y[smallerind]
            xgreater = self.X[greaterind]
            ygreater = self.Y[greaterind]
            slope = (ygreater - ysmaller) / (xgreater - xsmaller)
            value = ysmaller + slope * (point - xsmaller)
            predictions[pointidx] = value
        return predictions