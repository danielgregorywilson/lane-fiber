<template>
  <q-page class="q-pa-md">
    <div class="form-header">
      <div class="row justify-center">Fiber Cable</div>
      <div class="row justify-center">Complete form once for every cable reel</div>
    </div>
    <div class="row items-center q-gutter-md q-mt-xs">
      <div>Fiber Cable Location</div>
      <q-input dense filled v-model="fiberCableLocation" class="col"/>
    </div>
    <div class="row items-center q-gutter-md q-mt-xs">
      <div>Fiber Strand Count</div>
      <q-input dense filled v-model="fiberStrandCount" />
    </div>
    <div class="row items-center q-gutter-md q-mt-xs">
      <div>Buffer Tube/Strand Config</div>
      <q-option-group
        v-model="strandConfig"
        :options="strandConfigOptions"
        color="primary"
      />
    </div>
    <!-- TODO: Use regular radios so that we can put the 'other' inline with the third option -->
    <q-input dense filled v-model="fiberCableLocation" class="col"/>
    <div class="row justify-center">*Typical Tube Color Order = Blue, Orange, Green, Brown, Slate, White, Red, Black, Yellow, Violet, Rose, Aqua*</div>
    
    <hr />




Cable Type: ADSS Mini-Span ADSS Medium ADSS Transmission UG Armored
 Fiber Cable Location
 Fiber Strand Count
 Buffer Tube/Strand Config
    Infrastructure Class:
Foot Stamp Units: Foot
Meter
Pigtail
Foot Stamp No: _____________
Alcatel AT&T Belde Chromatic Tech Optical Cable Corp Prysmian/Pirelli
Other: ___________
OPGW
ABF Other: ______ Backbone Lateral
    Manufacturer: 3M AFL Telecom Draka USA OFS
Remmee Products Corp
 Manufacturer Catalog Number: ________________ Date: ________________ Owner: EWEB City LCOG SUB LEVEL 3 LSN Other: __________
Installer: EWEB MFS AstroTech Other: ________________
Additional Comments:__________________________________________________ __________________________________________________ __________________________________________________
  </q-page>
</template>

<style scoped>

</style>

<script lang="ts">
import axios from 'axios';
import { Component, Vue } from 'vue-property-decorator'

@Component({})
export default class Dashboard extends Vue {
  private fiberCableLocation = ''
  private fiberStrandCount = ''
  private strandConfig = ''
  private strandConfigOptions = [
    {
      label: 'Typical Tube Color Order – 12 strands/tube',
      value: '12'
    },
    {
      label: 'Typical Tube Color Order– 6 strands/tube',
      value: '6'
    },
    {
      label: 'Other',
      value: 'other'
    }
  ]
  private otherStrandConfig = ''

  
  
  
  private type = 'image'
  private title = ''
  private description = ''
  private date = ''

  private file = new File([''], '')
  private story = ''
  private successfulUpload = false

  private fieldsComplete(): boolean {
    return !!this.story || this.type != 'story'
  }

  private upload(): void {
    let fd = new FormData();
    fd.append('title', this.title)
    fd.append('description', this.description)
    if (!this.date) {
      this.date = ''
    }
    fd.append('date', this.date.split('/').join('-'))
    
    // const { type, title, description, date, file, story } = this
    switch(this.type) {
      case 'image':
        fd.append('image', this.file)
        axios({url: `${ process.env.API_URL }api/upload-image/`, data: fd, method: 'POST' }) // eslint-disable-line @typescript-eslint/restrict-template-expressions
          .then(() => {
            this.successfulUpload = true
          })
          .catch(e => {
            console.error('Error uploading image memory:', e)
          })
        break;
      case 'story':
        fd.append('story', this.story)
        axios({url: `${ process.env.API_URL }api/upload-story/`, data: fd, method: 'POST' }) // eslint-disable-line @typescript-eslint/restrict-template-expressions
          .then(() => {
            this.successfulUpload = true
          })
          .catch(e => {
            console.error('Error uploading story memory:', e)
          })
        break;
      case 'video':
        fd.append('video', this.file)
        axios({url: `${ process.env.API_URL }api/upload-video/`, data: fd, method: 'POST' }) // eslint-disable-line @typescript-eslint/restrict-template-expressions
          .then(() => {
            this.successfulUpload = true
          })
          .catch(e => {
            console.error('Error uploading video memory:', e)
          })
        break;
      case 'audio':
        fd.append('audio', this.file)
        axios({url: `${ process.env.API_URL }api/upload-audio/`, data: fd, method: 'POST' }) // eslint-disable-line @typescript-eslint/restrict-template-expressions
          .then(() => {
            this.successfulUpload = true
          })
          .catch(e => {
            console.error('Error uploading audio memory:', e)
          })
        break;
      default:
        // code block
    }
  }

};
</script>
