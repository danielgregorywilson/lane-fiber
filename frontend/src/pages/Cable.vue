<template>
  <q-page class="q-pa-md">
    <div class="form-header">
      <div class="row justify-center text-h4 text-bold">Fiber Cable</div>
      <div class="row justify-center">Complete form once for every cable reel</div>
    </div>
    <div class="row items-center q-gutter-md q-mt-xs">
      <div class="text-bold">Fiber Cable Location:</div>
      <q-input dense filled v-model="location" class="col"/>
    </div>
    <div class="row items-center q-gutter-md q-mt-xs">
      <div class="text-bold">Fiber Strand Count:</div>
      <q-input dense filled v-model="fiberStrandCount" />
    </div>
    <div class="row items-center q-gutter-md q-mt-xs">
      <div class="text-bold">Buffer Tube/Strand Config:</div>
      <div class="col">
        <div class="row">
          <q-radio v-model="strandConfig" val="12" label="Typical Tube Color Order – 12 strands/tube" />
        </div>
        <div class="row">
          <q-radio v-model="strandConfig" val="6" label="Typical Tube Color Order– 6 strands/tube" />
        </div>
        <div class="row">
          <q-radio v-model="strandConfig" val="other" label="Other" />
          <q-input dense filled v-if="strandConfig=='other'" v-model="otherStrandConfig" class="q-pl-sm"/>
        </div>
      </div>
    </div>
    <div class="row justify-center">*Typical Tube Color Order = Blue, Orange, Green, Brown, Slate, White, Red, Black, Yellow, Violet, Rose, Aqua*</div>
    
    <hr />

    <div class="row items-center q-gutter-md q-mt-xs">
      <div class="text-bold">Cable Type:</div>
      <div class="col">
        <div class="row">
          <q-radio v-model="cableType" val="ADSSMini" label="ADSS Mini-Span" />
          <q-radio v-model="cableType" val="ADSSMedium" label="ADSS Medium" />
          <q-radio v-model="cableType" val="ADSSTransmission" label="ADSS Transmission" />
          <q-radio v-model="cableType" val="UGArmored" label="UG Armored" />
          <q-radio v-model="cableType" val="OPGW" label="OPGW" />
          <q-radio v-model="cableType" val="ABF" label="ABF" />
          <div class="row">
            <q-radio v-model="cableType" val="other" label="Other" />
            <q-input dense filled v-if="cableType=='other'" v-model="otherCableType" class="q-pl-sm"/>
          </div>
        </div>
      </div>
    </div>
    <div class="row items-center q-gutter-md q-mt-xs">
      <div class="text-bold">Infrastructure Class:</div>
      <q-option-group
        v-model="infrastructureClass"
        :options="infrastructureClassOptions"
        inline
      />
    </div>
    <div class="row q-mt-xs items-center q-gutter-md">
      <div class="text-bold">Foot Stamp Units:</div>
      <q-option-group
        v-model="footStampUnits"
        :options="footStampUnitsOptions"
        inline
      />
    </div>
    <div class="row q-mt-xs items-center q-gutter-md">
      <div class="text-bold">Foot Stamp No:</div>
      <q-input dense filled v-model="footStampNumber" />
    </div>

    <hr />

    <div class="row items-center q-gutter-md q-mt-xs">
      <div class="text-bold">Manufacturer:</div>
      <div class="col">
        <div class="row">
          <q-radio v-model="manufacturer" val="3M" label="3M" />
          <q-radio v-model="manufacturer" val="AFL" label="AFL Telecom" />
          <q-radio v-model="manufacturer" val="alcatel" label="Alcatel" />
          <q-radio v-model="manufacturer" val="ATT" label="AT&T" />
          <q-radio v-model="manufacturer" val="belde" label="Belde" />
          <q-radio v-model="manufacturer" val="chromatic" label="Chromatic Tech" />
          <q-radio v-model="manufacturer" val="draka" label="Draka USA" />
          <q-radio v-model="manufacturer" val="OFS" label="OFS" />
          <q-radio v-model="manufacturer" val="OCC" label="Optical Cable Corp" />
          <q-radio v-model="manufacturer" val="prysmian" label="Prysmian/Pirelli" />
          <q-radio v-model="manufacturer" val="remmee" label="Remmee Products Corp" />
          <div class="row">
            <q-radio v-model="manufacturer" val="other" label="Other" />
            <q-input dense filled v-if="manufacturer=='other'" v-model="otherManufacturer" class="q-pl-sm"/>
          </div>
        </div>
      </div>
    </div>
    <div class="row q-mt-xs items-center q-gutter-md">
      <div class="text-bold">Manufacturer Catalog Number:</div>
      <q-input dense filled v-model="manufacturerCatalogNumber" />
    </div>
    <div class="row q-mt-xs items-center q-gutter-md">
      <div class="text-bold">Date:</div>
      <q-input dense filled v-model="date" />
    </div>

    <hr />
    
    <div class="row items-center q-gutter-md q-mt-xs">
      <div class="text-bold">Owner:</div>
      <div class="col">
        <div class="row">
          <q-radio v-model="owner" val="EWEB" label="EWEB" />
          <q-radio v-model="owner" val="city" label="City" />
          <q-radio v-model="owner" val="LCOG" label="LCOG" />
          <q-radio v-model="owner" val="SUB" label="SUB" />
          <q-radio v-model="owner" val="level3" label="LEVEL 3" />
          <q-radio v-model="owner" val="LSN" label="LSN" />
          <div class="row">
            <q-radio v-model="owner" val="other" label="Other" />
            <q-input dense filled v-if="owner=='other'" v-model="otherOwner" class="q-pl-sm"/>
          </div>
        </div>
      </div>
    </div>
    <div class="row items-center q-gutter-md q-mt-xs">
      <div class="text-bold">Installer:</div>
      <div class="col">
        <div class="row">
          <q-radio v-model="installer" val="EWEB" label="EWEB" />
          <q-radio v-model="installer" val="MFS" label="MFS" />
          <q-radio v-model="installer" val="astroTech" label="AstroTech" />
          <div class="row">
            <q-radio v-model="installer" val="other" label="Other" />
            <q-input dense filled v-if="installer=='other'" v-model="otherInstaller" class="q-pl-sm"/>
          </div>
        </div>
      </div>
    </div>

    <hr />

    <div class="row q-mt-xs items-center q-gutter-md">
      <div class="text-bold">Additional Comments:</div>
      <q-input filled dense autogrow type="textarea" v-model="comments" class="col" />
    </div>

    <q-btn label="Submit" :disable="!formComplete()" @click="submit" class="q-mt-md" />
    {{this.formComplete()}}

  </q-page>
</template>

<style scoped>

</style>

<script lang="ts">
import axios from 'axios';
import { Component, Vue } from 'vue-property-decorator'

@Component({})
export default class Dashboard extends Vue {
  private location = ''
  private fiberStrandCount = ''
  private strandConfig = ''
  private otherStrandConfig = ''
  private cableType = ''
  private otherCableType = ''
  private infrastructureClass = ''
  private infrastructureClassOptions = [
    {
      label: 'Backbone',
      value: 'backbone'
    },
    {
      label: 'Lateral',
      value: 'lateral'
    },
    {
      label: 'Pigtail',
      value: 'pigtail'
    }
  ]
  private footStampUnits = ''
  private footStampUnitsOptions = [
    {
      label: 'Foot',
      value: 'foor'
    },
    {
      label: 'Meter',
      value: 'meter'
    }
  ]
  private footStampNumber = ''
  private manufacturer = ''
  private otherManufacturer = ''
  private manufacturerCatalogNumber = ''
  private date = ''
  private owner = ''
  private otherOwner = ''
  private installer = ''
  private otherInstaller = ''
  private comments = ''
  
  private formComplete(): boolean {
    let checker = (arr: Array<boolean>) => arr.every(Boolean);
    return checker([
      !!this.location,
      !!this.fiberStrandCount,
      !!this.strandConfig,
      this.strandConfig != 'other' || !!this.otherStrandConfig,
      !!this.cableType,
      this.cableType != 'other' || !!this.otherCableType,
      !!this.infrastructureClass,
      !!this.footStampUnits,
      !!this.footStampNumber,
      !!this.manufacturer,
      this.manufacturer != 'other' || !!this.otherManufacturer,
      !!this.manufacturerCatalogNumber,
      !!this.date,
      !!this.owner,
      this.owner != 'other' || !!this.otherOwner,
      !!this.installer,
      this.installer != 'other' || !!this.otherInstaller
    ])
  }

  // private upload(): void {
  //   let fd = new FormData();
  //   fd.append('title', this.title)
  //   fd.append('description', this.description)
  //   if (!this.date) {
  //     this.date = ''
  //   }
  //   fd.append('date', this.date.split('/').join('-'))
    
  //   // const { type, title, description, date, file, story } = this
  //   switch(this.type) {
  //     case 'image':
  //       fd.append('image', this.file)
  //       axios({url: `${ process.env.API_URL }api/upload-image/`, data: fd, method: 'POST' }) // eslint-disable-line @typescript-eslint/restrict-template-expressions
  //         .then(() => {
  //           this.successfulUpload = true
  //         })
  //         .catch(e => {
  //           console.error('Error uploading image memory:', e)
  //         })
  //       break;
  //     case 'story':
  //       fd.append('story', this.story)
  //       axios({url: `${ process.env.API_URL }api/upload-story/`, data: fd, method: 'POST' }) // eslint-disable-line @typescript-eslint/restrict-template-expressions
  //         .then(() => {
  //           this.successfulUpload = true
  //         })
  //         .catch(e => {
  //           console.error('Error uploading story memory:', e)
  //         })
  //       break;
  //     case 'video':
  //       fd.append('video', this.file)
  //       axios({url: `${ process.env.API_URL }api/upload-video/`, data: fd, method: 'POST' }) // eslint-disable-line @typescript-eslint/restrict-template-expressions
  //         .then(() => {
  //           this.successfulUpload = true
  //         })
  //         .catch(e => {
  //           console.error('Error uploading video memory:', e)
  //         })
  //       break;
  //     case 'audio':
  //       fd.append('audio', this.file)
  //       axios({url: `${ process.env.API_URL }api/upload-audio/`, data: fd, method: 'POST' }) // eslint-disable-line @typescript-eslint/restrict-template-expressions
  //         .then(() => {
  //           this.successfulUpload = true
  //         })
  //         .catch(e => {
  //           console.error('Error uploading audio memory:', e)
  //         })
  //       break;
  //     default:
  //       // code block
  //   }
  // }

};
</script>
