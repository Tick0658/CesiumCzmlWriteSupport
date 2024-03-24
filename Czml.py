import pandas as pd


class Czml:
    
    class Position:
        # 配列に 3つの要素がある場合、値は定数です。
        # 4つ以上の要素がある場合、それらは [Time, X, Y, Z, Time, X, Y, Z, ...] のように配置された時間タグ付きサンプルです。
        # Time は ISO 8601 の日付と時刻の文字列または秒です。
        cartesian = {"cartesian": []}
        # 3 次元デカルト値 [X, Y, Z] として指定される位置 (referenceFrame を基準としたメートル単位)。
        cartographicRadians = {"cartographicRadians": []}
        # WGS84 座標 [経度、緯度、高さ] で指定された位置。経度と緯度はラジアン単位、高さはメートル単位
        cartographicDegrees = {"cartographicDegrees": []}
        # WGS84 座標 [経度、緯度、高さ] で指定された位置。経度と緯度は度数単位、高さはメートル単位

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

    
    class Properties:
        properties = {
            "properties": {
                "id": None,
                # このパケットに記述されているオブジェクトのID
                # IDはGUIDである必要はないが、CZMLソースや同じスコープにロードされた他の
                # CZMLソースの中で一つのオブジェクトを一意に識別する必要がある。
                "nama": None,
                # オブジェクトの名前。一意である必要はなく、ユーザーが使用するためのものです。
                "parent": None,
                # 親オブジェクトがある場合は、そのID。
                "description": None,
                # オブジェクトのHTML記述。
                "clock": {},
                # class clockを参照
                # データセット全体の時計設定。ドキュメントオブジェクトでのみ有効。
                "version": None,
                # 書き込まれるCZMLのバージョン
                "availability": "0000-00-00T00:00:00Z/9999-12-31T24:00:00Z",
                # オブジェクトのデータが利用可能な時間間隔のセット
                # このプロパティには、1つの時間間隔を表す文字列を指定することも、時間間隔を表す文字列の配列を指定することもできる
                "properties": {},
                # class CustomPropertyを参照
                # このオブジェクトのカスタムプロパティのセット。
                # この型はキーと値のマッピングを表し、値はCustomProperty型である。
                "position": {},
                # class Positionを参照
                # ワールド内のオブジェクトの位置。この位置は直接的な視覚的表現はないが、
                # ビルボードやラベルなど、オブジェクトに付属するグラフィカルなアイテムの位置を特定するために使用される。
                "orientation": {},
                # class Orientationを参照
                # ワールド内のオブジェクトの向き。方位は直接視覚的な表現を持たないが、モデル、円錐、ピラミッド、
                # その他オブジェクトに付属するグラフィカルアイテムを方向付けるために使用される。
                "viewFrom": {},
                #class ViewFrom参照
                #このオブジェクトを表示するときに推奨されるカメラの位置。このプロパティは、オブジェクトの位置を基準とした東 (x)、北 (y)、上 (z) 参照フレーム内のデカルト位置として指定されます。
                "billboard": {},
                #class Billboard参照
                #ビルボード、またはビューポートに位置合わせされたイメージ。マーカーとも呼ばれます。看板は敷地内のシーンに設置されていますposition。
                "box": {},
                #class Box参照
                #閉じた直方体であるボックス。ボックスの位置と方向は、positionと のorientationプロパティを使用して設定されます。
                "corridor": {},
                #class Corridor参照
                #コリドー。中心線と幅によって定義される形状です。
                "cylinder": {},
                #class Cylinder参照
               # 長さ、上部半径、下部半径によって定義される円柱、円錐台、または円錐。円柱の位置と方向は、positionと のorientationプロパティを使用して設定されます。
                "ellipse": {},
                #class Ellipse参照
                #地球の表面上の閉じた曲線である楕円。楕円はpositionプロパティを使用して配置されます。
                "ellipsoid": {},
                #class Ellipsoid参照
                #楕円体。楕円の 3 次元類似物である閉じた二次曲面です。
                # 楕円体の位置と方向は、positionおよびorientationプロパティを使用して設定されます。
                "label": {},
                #class label参照
                #テキストの文字列。ラベルはプロパティによってシーン内に配置されますposition。
                "model": {},
                #class Model参照
                #モデルの位置と方向は、positionと のorientationプロパティを使用して設定されます。
                "path": {},
                #class Path参照
                #時間の経過に伴うオブジェクトの動きによって定義されるポリラインです。
                # パスの可能な頂点はpositionプロパティによって指定されます。
                "point": {},
                #class Point参照
                #点、またはビューポートに位置合わせされた円。
                # ポイントはpositionプロパティによってシーン内に配置されます。
                "polygon": {},
                #class Polygon参照
                #地球の表面上の閉じた図形である多角形。
                "polyline": {},
                #class Polyline参照
                #ポリライン。複数のセグメントで構成されるシーン内の線です。
                "polylineVolume": {},
                #class PolylineVolume参照
                #ボリュームのあるポリライン。
                # ポリラインに沿って押し出された 2D 形状として定義されます。
                "rectangle": {},
                #class Rectangle参照
                #地図作成用の長方形。地球の曲率に適合し、地表に沿ってまたは高度に配置できます。
                "tileset": {},
                #class Tileset参照
                #3D タイルのタイルセット。
                "wall": {},
                # class Wall参照
                # 地球の曲率に適合し、地表に沿ってまたは高度に配置できる 2 次元の壁。
                "agi_conicSensor": {},
                # class Agi_conicSensor参照
                # 楕円体、つまり地球のオクルージョンを考慮した円錐形のセンサー ボリューム。
                # センサーの位置と方向は、positionと のorientationプロパティを使用して設定されます。
                "agi_customPatternSensor": {},
                #class Agi_customPatternSensor参照
                # 楕円体、つまり地球のオクルージョンを考慮したカスタム センサー ボリューム。
                # センサーの位置と方向は、positionと のorientationプロパティを使用して設定されます。
                "agi_rectangularSensor": {},
                #class Agi_rectangularSensor参照
                # 楕円体、つまり地球のオクルージョンを考慮した四角錐のセンサー ボリューム。
                # センサーの位置と方向は、positionと のorientationプロパティを使用して設定されます。
                "agi_fan": {},
                #class Agi_fan参照
                # 点または頂点から始まり、頂点から指定された方向のリストに広がるファンを定義します。
                # 方向の各ペアは、指定された半径まで広がるファンの面を形成します。
                # ファンは、positionと のorientationプロパティを使用して位置と方向を設定します。
                "agi_vector": {},
                #class Agi_vector参照
                # positionプロパティを起点とし、指定された方向に指定された長さだけ伸びるグラフィック ベクトルを定義します。
                # ベクトルはpositionプロパティを使用して配置されます。
            }
        }


def Czmlsuppoter():
    a = Czml.Path.path
    return a


a = Czmlsuppoter()
print(a["path"])
pass
