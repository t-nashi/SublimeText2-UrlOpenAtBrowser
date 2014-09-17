#-*-coding: utf-8 -*-						# utf-8エンコーディング（ファイル内日本語利用許可）

#API関数を使うためにライブラリのインポート
import sublime, sublime_plugin
import webbrowser
import re

#====================================================================
# アクティブファイル中の対象文字列の含まれている行をリストに収めてコンソール出力・ブラウザオープンする （super + ctfl + shift + O）
#====================================================================
class UrlOpenAtBrowserCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		# line_len にアクティブファイルの終了行番号を代入
		line_len, _ = self.view.rowcol(self.view.size())

		# 抽出したurlを格納する空リストの用意
		url_list = []

		# 正規表現パターンを定義してコンパイル
		p = re.compile('(https?://[-_.!~*\'()a-zA-Z0-9;/?:@&=+$,%#]+)')

		# アクティブファイルの始まりから終わりまで処理
		for region in range(0, line_len):
			# 行毎に開始位置を調べ、そこからその行の文字列を取得し「line_contents」へ代入
			pt = self.view.text_point(region, 0)
			line = self.view.line(pt)
			line_contents = self.view.substr(line)

			# 定義したパターンにマッチした文字列をリストへ格納
			for m in p.finditer(line_contents):
				if m:
					url_list += [m.group()]
					#print m.group()
				else:
					pass

		# urlを格納したリストを処理
		for i in url_list:
			if i:
				# ブラウザでurlを開く
				self.open_browser(i)
				# コンソールへ値を出力
				print i
			else:
				pass

	# ブラウザでurlを開くメソッド
	def open_browser(self, url):
		webbrowser.open(url)