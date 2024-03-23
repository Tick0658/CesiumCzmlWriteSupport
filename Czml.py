import pandas as pd


class Czml:
    class Path:
        path = {
            "path": {
                "leadTime": None,
                # アニメーション時間より進んでパスを表示する時間 (秒単位)。 この時間は、オブジェクトの可用性を超えないように制限されます。
                # デフォルトでは、値は無制限であり、事実上、オブジェクトの使用可能なパス全体が描画されることになります。
                "trailTime": None,
                # アニメーション時間からパスを表示するまでの時間 (秒単位)。 この時間は、オブジェクトの可用性を超えないように制限されます。
                # デフォルトでは、値は無制限であり、事実上、オブジェクトの使用可能なパス全体が描画されることになります。
                "width": 1.0,
                # パスラインの幅
                "resolution": 60.0,
                # パスのサンプリングに使用される最大ステップ サイズ (秒単位)。
                # 位置プロパティに解像度で指定したよりも離れたデータ ポイントがある場合、追加のサンプルが計算され、より滑らかなパスが作成されます。
                "material": {},
                # パスの描画に使用するマテリアル。
                # PolylineMaterialを指定します
                "distanceDisplayCondition": [150, 15000000],
                # このパスをカメラからどのくらいの距離で表示するかを指定する表示条件。
                # [NearDistance, FarDistance]
            }
        }

    class Label:
        LabelStyle = ["FILL", "OUTLINE", "FILL_AND_OUTLINE"]
        # FILL:ラベルのテキストが塗りつぶし、輪郭なし
        # OUTLINE:ラベルのテキストが塗りつぶしなし、輪郭あり
        # FILL_AND_OUTLINE:ラベルのテキストが塗りつぶし、輪郭あり

        HeightReference = ["NONE", "CLAMP_TO_GROUND", "RELATIVE_TO_GROUND"]
        # NONE:位置は絶対です。
        # CLAMP_TO_GROUND:位置は地形に固定されます。
        # RELATIVE_TO_GROUND:位置の高さは地形上の高さです。

        VerticalOrigin = ["CENTER", "BASELINE", "BOTTOM", "TOP"]
        # BASELINE:オブジェクトにテキストが含まれている場合、原点はテキストのベースラインにあり、それ以外の場合、原点はオブジェクトの下部にあります。
        # BOTTOM:原点はオブジェクトの下部にあります。
        # CENTER:原点は BASELINE と TOP の間の垂直方向の中心にあります
        # TOP:原点はオブジェクトの上部にあります。

        HorizontalOrigin = ["CENTER", "LEFT", "RIGHT"]
        # LEFT:原点はオブジェクトの左側にあります。
        # CENTER:原点はオブジェクトの水平方向の中心にあります。
        # RIGHT:原点はオブジェクトの右側にあります。

        label = {
            "label": {
                "text": "",
                # ラベルによって表示されるテキスト。 改行文字 (\n) は改行を示します。
                "font": "30px sans-serif",
                # CSS の「font」プロパティと同じ構文を使用して指定されるフォント。
                "style": LabelStyle[0],
                # 0:FILL, 1:OUTLINE", 2:FILL_AND_OUTLINE"
                # ラベルのスタイル。
                "scale": 1.0,
                # ラベルのスケール。
                # スケールは、ラベルのテキストのピクセル サイズで乗算されます。
                "showBackground": False,
                # ラベルの背景を表示するかどうか。
                "backgroundColor": {},
                # ラベルの背景の色。
                # colorを指定
                "backgroundPadding": [7, 5],
                # テキストとラベルの背景の間のパディングの量。
                "pixelOffset": [0.0, 0.0],
                # 位置からのラベル原点のオフセット (ビューポート ピクセル単位)。
                "eyeOffset": [0.0, 0.0, 0.0],
                # ラベルの目のオフセット。位置プロパティを基準にしてラベルを配置する目の座標のオフセットです。
                "horizontalOrigin": HorizontalOrigin[0],
                # ラベルの水平方向の原点。 ラベルを位置に対して左揃え、中央揃え、または右揃えにするかを制御します。
                "verticalOrigin": VerticalOrigin[0],
                # オブジェクトの位置に対する原点の垂直方向の位置。
                "heightReference": HeightReference[0],
                # ラベルの高さの参照。位置が地形に対して相対的であるかどうかを示します。
                "fillColor": {},
                # 塗りつぶしの色　colorを指定
                "outlineColor": {},
                # 輪郭の色　colorを指定
                "outlineWidth": 1.0,
                # 輪郭の太さ
                "translucencyByDistance": [150, 2.0, 15000000, 0.5],
                # ラベルのカメラからの距離に基づいて、ラベルの半透明度がどのように変化するか。
                # このスカラー値の範囲は 0 ～ 1 である必要があります。
                "pixelOffsetScaleByDistance ": [150, 2.0, 15000000, 0.5],
                # ラベルのカメラからの距離に基づいて、ラベルのピクセル オフセットをどのように変更するか。
                # このスカラー値は、pixelOffset で乗算されます。
                # [NearDistance, NearValue, FarDistance, FarValue]
                "scaleByDistance": [150, 2.0, 15000000, 0.5],
                # カメラからのラベルの距離に基づいてラベルのスケールをどのように変更するか。
                # このスカラー値はスケールで乗算されます。
                # [NearDistance, NearValue, FarDistance, FarValue]
                "distanceDisplayCondition": [150, 15000000],
                # このパスをカメラからどのくらいの距離で表示するかを指定する表示条件。
                # [NearDistance, FarDistance]
                "disableDepthTestDistance": 0.0,
                # 深度テストを無効にするカメラからの距離。
                # これは、たとえば地形に対するクリッピングを防ぐために使用できます。
                # ゼロに設定すると、深度テストが常に適用されます。 Infinity に設定すると、深度テストは適用されません。
            }
        }

    class Position:
        #配列に 3つの要素がある場合、値は定数です。 
        #4つ以上の要素がある場合、それらは [Time, X, Y, Z, Time, X, Y, Z, ...] のように配置された時間タグ付きサンプルです。
        # Time は ISO 8601 の日付と時刻の文字列または秒です。
        cartesian = {"cartesian": []}
        #3 次元デカルト値 [X, Y, Z] として指定される位置 (referenceFrame を基準としたメートル単位)。
        cartographicRadians ={"cartographicRadians":[]}
        #WGS84 座標 [経度、緯度、高さ] で指定された位置。経度と緯度はラジアン単位、高さはメートル単位
        cartographicDegrees={"cartographicDegrees":{}}
        #WGS84 座標 [経度、緯度、高さ] で指定された位置。経度と緯度は度数単位、高さはメートル単位


def Czmlsuppoter():
    a = Czml.Path.path
    return a


a = Czmlsuppoter()
print(a["path"])
pass
