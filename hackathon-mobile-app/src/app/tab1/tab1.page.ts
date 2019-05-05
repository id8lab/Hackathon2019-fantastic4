import { Component, NgZone } from '@angular/core';

import { AlertController } from '@ionic/angular';
import { HttpClient } from '@angular/common/http';
import { SpeechRecognition } from '@ionic-native/speech-recognition';

@Component({
  selector: 'app-tab1',
  templateUrl: 'tab1.page.html',
  styleUrls: ['tab1.page.scss']
})
export class Tab1Page {

  isListening = false;
  matches: Array<string>;

  constructor(
    private http: HttpClient,
    private alertController: AlertController
    // ,
    // private speech: SpeechRecognition,
    // private zone: NgZone
  ) {

  }

  sendData(command) {
    console.log('button gets clicked');
    // 192.168.1.86
    this.http.get(`http://10.175.10.197/send-data?command=${command}`).subscribe(data => {
      console.log('data');
      console.log(data);

      this.presentAlert(JSON.stringify(data));
    }, err => {
      console.log('err');
      console.log(err);
    });
  }

  getDistance() {
    this.sendData('GetDistance');
  }

  getTemperatureHumidity() {
    this.sendData('TemperatureHumidity');
  }

  openLight() {
    this.sendData('OpenLight');
  }

  closeLight() {
    this.sendData('CloseLight');
  }

  lockDoor() {
    this.sendData('LockDoor');
  }

  unlockDoor() {
    this.sendData('UnlockDoor');
  }

  // searchCordova() {
  //   window['plugins'].speechRecognition.hasPermission(permission => {

  //     if (!permission) {
  //       window['plugins'].speechRecognition.requestPermission(_ => {
  //         window['plugins'].speechRecognition.startListening(terms => {
  //           if (terms && terms.length > 0) {
  //             // this.movieSearch([terms[0]]);
  //             console.log(terms[0]);
  //           } else {
  //             // this.movieSearch(terms);
  //             console.log(terms);
  //           }
  //         });
  //       });
  //     } else {
  //       window['plugins'].speechRecognition.startListening(terms => {
  //         if (terms && terms.length > 0) {
  //           // this.movieSearch([terms[0]]);
  //           console.log(terms[0]);
  //         } else {
  //           // this.movieSearch(terms);
  //           console.log(terms);
  //         }
  //       });
  //     }
  //   });
  // }

  async presentAlert(data) {
    const alert = await this.alertController.create({
      header: 'Alert',
      subHeader: 'Response from API',
      message: data,
      buttons: ['OK']
    });

    await alert.present();
  }

}
