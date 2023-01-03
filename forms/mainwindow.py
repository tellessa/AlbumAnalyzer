from PySide6.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QLabel, QPushButton
from PySide6.QtGui import QPixmap

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
        button_get_track_features.setToolTip("Get Audio Features for the specified track URI")
        button_get_track_features.clicked.connect(self.get_track_features)

        self.text_holder_label = QLabel("I AM HERE")
        h_layout = QHBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(self.line_edit)

        self.v_layout = QVBoxLayout()
        self.v_layout.addLayout(h_layout)
        self.v_layout.addWidget(button_get_track_features)

        pixmap = QPixmap("C:\\Users\\StephenTelles\\Documents\\images\\Short Ignitor WS001-0007.png")

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        self.move(300, 200)
        self.setWindowTitle('Image with PyQt')
        self.show()

        image_h_layout = QHBoxLayout()
        image_h_layout.addWidget(lbl)
        self.v_layout.addLayout(image_h_layout)

        self.setLayout(self.v_layout)

    def get_track_features(self):
        """TODO: Get the features of the song specified by the line edit's current text"""
        # spotipy_audio_features_for_track.get_fire_on_the_cathedral_features()
        self.text_holder_label.setText(self.line_edit.text())
        self.v_layout.addWidget(self.text_holder_label)
        track_id = self.line_edit.text()
        if track_id == "":
            # fallback for when we want to test without pasting in a specific song
            track_id = 'spotify:track:6Rskc4RUqPgmcxkQic0a5G'
        features = spotipy_audio_features_for_track.get_audio_features(track_id)

        self._create_key_labels()
        self._set_audio_feature_tool_tips()
        self._create_value_labels()
        for i, label in enumerate(self.key_labels):
            property_h_layout = QHBoxLayout()
            property_h_layout.addWidget(label)
            # add the corresponding value label to the same row of the layout
            property_h_layout.addWidget(self.value_labels[i])
            self.v_layout.addLayout(property_h_layout)
        # Fire on the Cathedral by Sun Theater
        # features = spotipy_audio_features_for_track.get_audio_features("spotify:track:6Rskc4RUqPgmcxkQic0a5G")
        # Gloria by Michael Telles
        # features = spotipy_audio_features_for_track.get_audio_features("spotify:track:6eT3lO8HbGMmDftI5aIY1T")
        self._show_track_features(features)

    def _show_track_features(self, features):
        self.danceability_value_label.setText(str(features["danceability"]))
        self.energy_value_label.setText(str(features["energy"]))
        keys = ["C", "C#/D♭", "D", "D#/E♭", "E", "F", "F#/G♭", "G", "G#/A♭", "A", "A#/B♭", "B"]
        # Use the key as an index to map integers to pitches, zero-indexed
        self.key_value_label.setText((keys[features["key"] + 1]))
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

    def _create_key_labels(self):
        # key labels
        self.danceability_key_label = QLabel("DANCEABILITY".title())
        self.energy_key_label = QLabel("ENERGY".title())
        self.key_key_label = QLabel("KEY".title())
        self.loudness_key_label = QLabel("Loudness")
        self.mode_key_label = QLabel("Mode")
        self.acousticness_key_label = QLabel("Acousticness")
        self.instrumentalness_key_label = QLabel("Instrumentalness")
        self.speechiness_key_label = QLabel("Speechiness")
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

    def _set_audio_feature_tool_tips(self):
        self.danceability_key_label.setToolTip(
            'Danceability describes how suitable a track is for dancing based on a combination of musical ' +
            'elements including tempo, rhythm stability, beat strength, and overall regularity. A value ' +
            'of 0.0 is least danceable and 1.0 is most danceable.'
        )
        self.energy_key_label.setToolTip(
            'Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and ' +
            'activity. Typically, energetic tracks feel fast, loud, and noisy. For example, death metal has ' +
            'high energy, while a Bach prelude scores low on the scale. Perceptual features contributing to ' +
            'this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy.'
        )
        self.key_key_label.setToolTip(
            'The key the track is in. Integers map to pitches using standard Pitch Class notation. ' +
            'E.g. 0 = C, 1 = C♯/D♭, 2 = D, and so on. If no key was detected, the value is -1.'
        )
        self.loudness_key_label.setToolTip(
            'The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track ' +
            'and are useful for comparing relative loudness of tracks. Loudness is the quality of a sound that is ' +
            'the primary psychological correlate of physical strength (amplitude). Values typically range between ' +
            '-60 and 0 db.')
        self.mode_key_label.setToolTip(
            'Mode indicates the modality (major or minor) of a track, the type of scale from which its melodic ' +
            'content is derived. Major is represented by 1 and minor is 0.')
        self.speechiness_key_label.setToolTip(
            'Speechiness detects the presence of spoken words in a track. The more ' +
            'exclusively speech-like the recording (e.g. talk show, audio book, poetry), ' +
            'the closer to 1.0 the attribute value. Values above 0.66 describe tracks ' +
            'that are probably made entirely of spoken words. Values between 0.33 ' +
            'and 0.66 describe tracks that may contain both music and speech, ' +
            'either in sections or layered, including such cases as rap music. Values ' +
            'below 0.33 most likely represent music and other non-speech-like tracks.'
        )
        self.acousticness_key_label.setToolTip(
            "A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence" +
            " the track is acoustic.")
        self.instrumentalness_key_label.setToolTip(
            'Predicts whether a track contains no vocals. "Ooh" and "aah" sounds are treated as instrumental in ' +
            'this context. Rap or spoken word tracks are clearly "vocal". The closer the instrumentalness value ' +
            'is to 1.0, the greater likelihood the track contains no vocal content. Values above 0.5 are intended ' +
            'to represent instrumental tracks, but confidence is higher as the value approaches 1.0.')
        self.liveness_key_label.setToolTip(
            'Detects the presence of an audience in the recording. Higher liveness values represent an ' +
            'increased probability that the track was performed live. A value above 0.8 provides strong likelihood ' +
            'that the track is live.')
        self.valence_key_label.setToolTip(
            'A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with ' +
            'high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence ' +
            'sound more negative (e.g. sad, depressed, angry).'
        )
        self.tempo_key_label.setToolTip(
            'The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo ' +
            'is the speed or pace of a given piece and derives directly from the average beat duration.'
        )
        self.type_key_label.setToolTip('The object type.')
        self.id_key_label.setToolTip(
            'The Spotify ID for the track.')
        self.uri_key_label.setToolTip('The Spotify URI for the track.')
        self.track_href_key_label.setToolTip('A link to the Web API endpoint providing full details of the track.')
        self.analysis_url_key_label.setToolTip(
            'A URL to access the full audio analysis of this track. An access token is required to access this data.'
        )
        self.duration_key_label.setToolTip(
            'The duration of the track in milliseconds.'
        )
        self.time_signature_key_label.setToolTip('An estimated time signature. The time signature (meter) is a notational ' +
                                                 'convention to specify how many beats are in each bar ( or measure). The ' +
                                                 'time signature ranges from 3 to 7 indicating time signatures of "3/4", to "7/4"')

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


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    from forms.mainwindow import MainWindow
    import sys

    app = QApplication(sys.argv)

    window = MainWindow(app)
    window.show()

    app.exec()
