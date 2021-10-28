import numpy as np
from pathlib import Path
import pkg_resources
from ..Raster import Raster, RasterStack
from ..Rasterize import rasterize


# Find path to data within the package
pth = Path(pkg_resources.resource_filename('rraster', 'data'))


class TestRaster:
    r1 = Raster(np.array([[1, 2, 3], [4, 5, 6]]), nodata=np.nan, transform=None, dtype='float32')
    r2 = Raster(np.array([[7, 8, 9], [10, 11, 12]]), nodata=np.nan, transform=None, dtype='float32')

    def test_add(self):
        tmp = self.r1 + self.r2
        assert (tmp.arr == np.array([[8, 10, 12], [14, 16, 18]])).all()

    def test_sub(self):
        tmp = self.r1 - self.r2
        assert (tmp.arr == np.array([[-6, -6, -6], [-6, -6, -6]])).all()

    def test_div(self):
        tmp = self.r1 / self.r2
        assert np.allclose(tmp.arr, np.array([[0.14285714, 0.25, 0.33333333], [0.4, 0.45454545, 0.5]]))

    def test_mul(self):
        tmp = self.r1 * self.r2
        assert (tmp.arr == np.array([[7, 16, 27], [40, 55, 72]])).all()

    def test_reproject(self):
        r1 = Raster(pth / '19990601_pr.tif')
        r2 = Raster(pth / 'template.tif')
        tmp = r1.reproject(r2)

        assert r2.arr.shape == tmp.arr.shape, 'Shapes are not the same.'
        assert r2.transform == tmp.transform, 'Transforms are not the same.'
        assert r2.crs == tmp.crs, 'CRS are not the same.'

    def test_write(self, tmp_path):
        fname = tmp_path / 'test.tif'
        self.r1.write(fname)
        assert fname.exists()

    def test_stack(self):
        stk = RasterStack(self.r1, self.r2)
        tmp = stk.reduce(np.mean, axis=0)

        assert np.allclose(tmp.arr, np.array([[4, 5, 6], [7, 8, 9]]))
