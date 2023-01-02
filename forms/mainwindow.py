from PySide6.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QLabel, QPushButton

from apis import spotipy_audio_features_for_track


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Spotify Audio Features")

        # A set of signals we can connect to
        label = QLabel("Track URI : ")
        self.line_edit = QLineEdit()
        # self.line_edit.textChanged.connect(self.text_changed)
        # self.line_edit.cursorPositionChanged.connect(self.cursor_position_changed)
        # self.line_edit.editingFinished.connect(self.editing_finished)
        self.line_edit.returnPressed.connect(self.return_pressed)
        # self.line_edit.selectionChanged.connect(self.selection_changed)
        self.line_edit.textEdited.connect(self.text_edited)

        button_get_track_features = QPushButton("Get Audio Features")
        button_get_track_features.setToolTip("Get Audio Features for Fire on The Cathedral by Sun Theater")
        button_get_track_features.clicked.connect(self.get_track_features)

        self._create_key_labels()
        self._create_value_labels()

        h_layout = QHBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(self.line_edit)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(button_get_track_features)
        v_layout.addWidget(self.text_holder_label)

        for i, label in enumerate(self.key_labels):
            property_h_layout = QHBoxLayout()
            property_h_layout.addWidget(label)
            # add the corresponding value label to the same row of the layout
            property_h_layout.addWidget(self.value_labels[i])
            v_layout.addLayout(property_h_layout)

        self.setLayout(v_layout)

#         # action1 = QAction("Get Whole Album Features", self)
#         # action1.setStatusTip("Use the Spotify API to get the album features for A Beautiful Letdown")
#         # action1.triggered.connect(lambda: self.toolbar_button_click(
#         #     spotipy_audio_features_for_track.get_whole_album_features))
#         # toolbar.addAction(action1)

#         # action2 = QAction(QIcon("start.png"), "Get Track Features", self)
#         # action2.setStatusTip("Getting Track Features")
#         # action2.triggered.connect(lambda: self.toolbar_button_click(self.get_track_features))
#         # # action2.setCheckable(True)
#         # toolbar.addAction(action2)

    def _create_key_labels(self):
        # key labels
        self.text_holder_label = QLabel("I AM HERE")
        self.danceability_key_label = QLabel("DANCEABILITY".title())
        self.energy_key_label = QLabel("ENERGY".title())
        self.key_key_label = QLabel("KEY".title())
        self.loudness_key_label = QLabel("Loudness")
        self.mode_key_label = QLabel("Mode")
        self.speechiness_key_label = QLabel("Speechiness")
        self.acousticness_key_label = QLabel("Acousticness")
        self.instrumentalness_key_label = QLabel("Instrumentalness")
        self.liveness_key_label = QLabel("Liveness")
        self.valence_key_label = QLabel("Valence")
        self.tempo_key_label = QLabel("Tempo")
        self.type_key_label = QLabel("Type")
        self.id_key_label = QLabel("Id")
        self.uri_key_label = QLabel("URI")
        self.track_href_key_label = QLabel("Track_HREF")
        self.analysis_url_key_label = QLabel("Analysis URL")
        self.duration_key_label = QLabel("Duration in ms")
        self.time_signature_key_label = QLabel("Time Signature")

        self.key_labels = [
            self.danceability_key_label,
            self.energy_key_label,
            self.key_key_label,
            self.loudness_key_label,
            self.mode_key_label,
            self.speechiness_key_label,
            self.acousticness_key_label,
            self.instrumentalness_key_label,
            self.liveness_key_label,
            self.valence_key_label,
            self.tempo_key_label,
            self.type_key_label,
            self.id_key_label,
            self.uri_key_label,
            self.track_href_key_label,
            self.analysis_url_key_label,
            self.duration_key_label,
            self.time_signature_key_label
        ]

    def _create_value_labels(self):
        # value labels
        self.danceability_value_label = QLabel("pending...")
        self.energy_value_label = QLabel("pending...")
        self.key_value_label = QLabel("pending...")
        self.loudness_value_label = QLabel("pending...")
        self.mode_value_label = QLabel("pending...")
        self.speechiness_value_label = QLabel("pending...")
        self.acousticness_value_label = QLabel("pending...")
        self.instrumentalness_value_label = QLabel("pending...")
        self.liveness_value_label = QLabel("pending...")
        self.valence_value_label = QLabel("pending...")
        self.tempo_value_label = QLabel("pending...")
        self.type_value_label = QLabel("pending...")
        self.id_value_label = QLabel("pending...")
        self.uri_value_label = QLabel("pending...")
        self.track_href_value_label = QLabel("pending...")
        self.analysis_url_value_label = QLabel("pending...")
        self.duration_value_label = QLabel("pending...")
        self.time_signature_value_label = QLabel("pending...")

        self.value_labels = [
            self.danceability_value_label,
            self.energy_value_label,
            self.key_value_label,
            self.loudness_value_label,
            self.mode_value_label,
            self.speechiness_value_label,
            self.acousticness_value_label,
            self.instrumentalness_value_label,
            self.liveness_value_label,
            self.valence_value_label,
            self.tempo_value_label,
            self.type_value_label,
            self.id_value_label,
            self.uri_value_label,
            self.track_href_value_label,
            self.analysis_url_value_label,
            self.duration_value_label,
            self.time_signature_value_label
        ]

    def get_track_features(self):
        """TODO: Get the features of the song specified by the line edit's current text"""
        # spotipy_audio_features_for_track.get_fire_on_the_cathedral_features()
        self.text_holder_label.setText(self.line_edit.text())
        track_id = self.line_edit.text()
        features = spotipy_audio_features_for_track.get_audio_features(track_id)
        # Fire on the Cathedral by Sun Theater
        # features = spotipy_audio_features_for_track.get_audio_features("spotify:track:6Rskc4RUqPgmcxkQic0a5G")
        # Gloria by Michael Telles
        # features = spotipy_audio_features_for_track.get_audio_features("spotify:track:6eT3lO8HbGMmDftI5aIY1T")
        self._show_track_features(features)

    def _show_track_features(self, features):
        self.danceability_value_label.setText(str(features["danceability"]))
        self.energy_value_label.setText(str(features["energy"]))
        self.key_value_label.setText(str(features["key"]))
        self.loudness_value_label.setText(str(features["loudness"]))
        self.mode_value_label.setText(str(features["mode"]))
        self.speechiness_value_label.setText(str(features["speechiness"]))
        self.acousticness_value_label.setText(str(features["acousticness"]))
        self.instrumentalness_value_label.setText(str(features["instrumentalness"]))
        self.liveness_value_label.setText(str(features["liveness"]))
        self.valence_value_label.setText(str(features["valence"]))
        self.tempo_value_label.setText(str(features["tempo"]))
        self.type_value_label.setText(str(features["type"]))
        self.id_value_label.setText(str(features["id"]))
        self.uri_value_label.setText(str(features["uri"]))
        self.track_href_value_label.setText(str(features["track_href"]))
        self.analysis_url_value_label.setText(str(features["analysis_url"]))
        self.duration_value_label.setText(str(features["duration_ms"]))
        self.time_signature_value_label.setText(str(features["time_signature"]))

    # Slots
    def button_clicked(self):
        # print("Fullname : ",self.line_edit.text())
        self.text_holder_label.setText(self.line_edit.text())

    def text_changed(self):
        print("Text  changed to ", self.line_edit.text())
        self.text_holder_label.setText(self.line_edit.text())

    def cursor_position_changed(self, old, new):
        print("cursor old position : ", old, " -new position : ", new)

    def editing_finished(self):
        print("Editing finished")

    def return_pressed(self):
        print("Return pressed")

    def selection_changed(self):
        print("Selection Changed : ", self.line_edit.selectedText())

    def text_edited(self, new_text):
        print("Text edited. New text : ", new_text)


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    from forms.mainwindow import MainWindow
    import sys

    app = QApplication(sys.argv)

    window = MainWindow(app)
    window.show()

    app.exec()
