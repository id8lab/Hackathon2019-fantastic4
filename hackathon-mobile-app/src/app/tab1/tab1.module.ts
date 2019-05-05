import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { IonicModule } from '@ionic/angular';
import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { SpeechRecognition } from '@ionic-native/speech-recognition/ngx';
import { Tab1Page } from './tab1.page';

@NgModule({
  imports: [
    IonicModule,
    CommonModule,
    FormsModule,
    RouterModule.forChild([{ path: '', component: Tab1Page }]),
    HttpClientModule
  ],
  declarations: [Tab1Page],
  providers: [
    SpeechRecognition
  ]

})
export class Tab1PageModule {}
