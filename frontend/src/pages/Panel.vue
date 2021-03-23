<template>
  <q-page class="q-pa-md">
    <div class="form-header">
      <div class="row justify-center text-h4 text-bold">Patch Panel</div>
      <div class="row justify-center">Complete form once for every patch panel</div>
    </div>
    <div class="row items-center q-gutter-md q-mt-xs">
      <div class="text-bold">Patch Panel Location Description:</div>
      <q-input dense filled v-model="location" class="col"/>
    </div>

    <hr />

    <div class="row items-center q-gutter-md q-mt-xs">
      <div class="text-bold">Owner:</div>
      <div class="col">
        <div class="row">
          <q-radio v-model="owner" val="EWEB" label="EWEB" />
          <q-radio v-model="owner" val="4J" label="4J SD" />
          <q-radio v-model="owner" val="bethel" label="Bethel SD" />
          <q-radio v-model="owner" val="ESD" label="Lane ESD" />
          <q-radio v-model="owner" val="LTD" label="LTD" />
          <q-radio v-model="owner" val="LCOG" label="LCOG" />
          <q-radio v-model="owner" val="eugene" label="City of Eugene" />
          <q-radio v-model="owner" val="springfield" label="City of Springfield" />
          <q-radio v-model="owner" val="lane" label="Lane County" />
          <q-radio v-model="owner" val="SUB" label="SUB" />
          <q-radio v-model="owner" val="level3" label="Level 3" />
          <q-radio v-model="owner" val="UO" label="U of O" />
          <div class="row">
            <q-radio v-model="owner" val="other" label="Other" />
            <q-input dense filled v-if="owner=='other'" v-model="otherOwner" class="q-pl-sm"/>
          </div>
        </div>
      </div>
    </div>

    <hr />

    <div class="row items-center q-gutter-md q-mt-xs">
      <div class="text-bold">Mount Type:</div>
      <q-option-group
        v-model="mountType"
        :options="mountTypeOptions"
        inline
      />
    </div>
    <div class="row items-center q-gutter-md q-mt-xs">
      <div class="text-bold">Installation Type:</div>
      <q-option-group
        v-model="installationType"
        :options="installationTypeOptions"
        inline
      />
    </div>
    <div class="row items-center q-gutter-md q-mt-xs">
      <div class="text-bold">Location:</div>
      <q-option-group
        v-model="locationType"
        :options="locationTypeOptions"
        inline
      />
    </div>

    <hr />

    <div class="row items-center q-gutter-md q-mt-xs">
      <div class="text-bold">Number of Card Rows:</div>
      <q-input dense filled v-model="cardRows" />
    </div>
    <div class="row items-center q-gutter-md q-mt-xs">
      <div class="text-bold">Number of Card Columns:</div>
      <q-input dense filled v-model="cardColumns" />
    </div>
    <div class="row items-center q-gutter-md q-mt-xs">
      <div class="text-bold">Slot Orientation:</div>
      <q-option-group
        v-model="slotOrientation"
        :options="slotOrientationOptions"
        inline
      />
    </div>
    <div class="row items-center q-gutter-md q-mt-xs">
      <div class="text-bold">Number of Ports per Card:</div>
      <q-input dense filled v-model="portsPerCard" />
    </div>
    <div class="row items-center q-gutter-md q-mt-xs">
      <div class="text-bold">Port Type:</div>
      <div class="col">
        <div class="row">
          <q-radio v-model="portType" val="SC" label="SC" />
          <q-radio v-model="portType" val="LC" label="LC" />
          <q-radio v-model="portType" val="ST" label="ST" />
          <div class="row">
            <q-radio v-model="portType" val="other" label="Other" />
            <q-input dense filled v-if="portType=='other'" v-model="otherPortType" class="q-pl-sm"/>
          </div>
        </div>
      </div>
    </div>
    <div class="row items-center q-gutter-md q-mt-xs">
      <div class="text-bold">Panel Installation Date:</div>
      <q-input dense filled v-model="installationDate" mask="date" :rules="['date']">
        <template v-slot:append>
          <q-icon name="event" class="cursor-pointer">
            <q-popup-proxy ref="qDateProxy" transition-show="scale" transition-hide="scale">
              <q-date v-model="installationDate">
                <div class="row items-center justify-end">
                  <q-btn v-close-popup label="Close" color="primary" flat />
                </div>
              </q-date>
            </q-popup-proxy>
          </q-icon>
        </template>
      </q-input>
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
    <div class="row items-center q-gutter-md q-mt-xs">
      <div class="text-bold">Model Number:</div>
      <div class="col">
        <div class="row">
          <q-radio v-model="model" val="BJ-1346" label="BJ-1346" />
          <q-radio v-model="model" val="CCH-04U" label="CCH-04U" />
          <q-radio v-model="model" val="FDC-001" label="FDC-001" />
          <q-radio v-model="model" val="FDC-002" label="FDC-002" />
          <q-radio v-model="model" val="FDC-005F" label="FDC-005F" />
          <q-radio v-model="model" val="FL2000" label="FL2000" />
          <q-radio v-model="model" val="WDC-001" label="WDC-001" />
          <q-radio v-model="model" val="WDC-002" label="WDC-002" />
          <div class="row">
            <q-radio v-model="model" val="other" label="Other" />
            <q-input dense filled v-if="model=='other'" v-model="otherModel" class="q-pl-sm"/>
          </div>
        </div>
      </div>
    </div>

    <hr />

    <div class="row q-mt-xs items-center q-gutter-md">
      <div class="text-bold">Additional Comments:</div>
      <q-input filled dense autogrow type="textarea" v-model="comments" class="col" />
    </div>

    <hr />

    <div class="row q-mt-xs items-center q-gutter-md">
      <div class="col">
        <div class="text-bold">Checklist:</div>
        <q-option-group
          v-model="checklistGroup"
          :options="checklistOptions"
          type="checkbox"
          class="q-ml-xs"
        />
      </div>
    </div>

    <q-btn label="Submit" :disable="!formComplete() || submitting" @click="submit" class="q-mt-md">
      <q-spinner-cube v-if="submitting" class="q-ml-sm" />
    </q-btn>

    <!-- Dialog to confirm successful submission -->
    <q-dialog v-model="showSuccessfulSubmissionDialog" persistent>
      <q-card>
        <q-card-section class="row items-center">
          <q-avatar icon="check" color="primary" text-color="white" />
          <div class="col">
            <span class="q-ml-sm row">Your submission has been received!</span>
          </div>
        </q-card-section>

        <q-card-actions align="right">
          <q-btn flat label="Return to Dashboard" color="primary" @click="navigateToDashboard()" />
          <q-btn flat label="Make another submission" color="primary" @click="submitAgain()" />
        </q-card-actions>
      </q-card>
    </q-dialog>

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
  private owner = ''
  private otherOwner = ''
  private mountType = ''
  private mountTypeOptions = [
    {
      label: 'Rack',
      value: 'rack'
    },
    {
      label: 'Frame',
      value: 'frame'
    },
    {
      label: 'Cabinet',
      value: 'cabinet'
    }
  ]
  private installationType = ''
  private installationTypeOptions = [
    {
      label: 'Free Standing',
      value: 'free'
    },
    {
      label: 'Wall Mount',
      value: 'wall'
    },
  ]
  private locationType = ''
  private locationTypeOptions = [
    {
      label: 'Indoors',
      value: 'indoors'
    },
    {
      label: 'Outdoors',
      value: 'outdoors'
    },
  ]
  private cardRows = ''
  private cardColumns = ''
  private slotOrientation = ''
  private slotOrientationOptions = [
    {
      label: 'Horizontal',
      value: 'horizontal'
    },
    {
      label: 'Vertical',
      value: 'vertical'
    },
  ]
  private portsPerCard = ''
  private portType = ''
  private otherPortType = ''
  private installationDate = ''
  private installer = ''
  private otherInstaller = ''
  private model = ''
  private otherModel = ''
  private comments = ''
  private checklistGroup: Array<string> = []
  private checklistOptions = [
    {
      label: 'Fill In Form',
      value: 'form'
    },
    {
      label: 'Take Photo',
      value: 'photo'
    },
    {
      label: 'Gather Termination Info',
      value: 'gatherInfo'
    }
  ]

  private submitting = false
  private showSuccessfulSubmissionDialog = false
  
  private formComplete(): boolean {
    let checker = (arr: Array<boolean>) => arr.every(Boolean);
    return checker([
      !!this.location,
      !!this.owner,
      this.owner != 'other' || !!this.otherOwner,
      !!this.mountType,
      !!this.installationType,
      !!this.locationType,
      !!this.cardRows,
      !!this.cardColumns,
      !!this.slotOrientation,
      !!this.portsPerCard,
      !!this.portType,
      this.portType != 'other' || !!this.otherPortType,
      !!this.installationDate,
      !!this.installer,
      this.installer != 'other' || !!this.otherInstaller,
      !!this.model,
      this.model != 'other' || !!this.otherModel,
      this.checklistGroup.indexOf('form') != -1,
      this.checklistGroup.indexOf('photo') != -1,
      this.checklistGroup.indexOf('gatherInfo') != -1
    ])
  }

  private submit(): void {
    this.submitting = true
    let fd = new FormData();
    fd.append('location', this.location)
    fd.append('owner', this.owner)
    if (this.owner == 'other') {
      fd.append('other_owner', this.otherOwner)
    }
    fd.append('mount_type', this.mountType)
    fd.append('installation_type', this.installationType)
    fd.append('location_type', this.locationType)
    fd.append('card_rows', this.cardRows)
    fd.append('card_columns', this.cardColumns)
    fd.append('slot_orientation', this.slotOrientation)
    fd.append('ports_per_card', this.portsPerCard)
    fd.append('port_type', this.portType)
    if (this.portType == 'other') {
      fd.append('other_port_type', this.otherPortType)
    }
    fd.append('installation_date', this.installationDate.split('/').join('-'))
    fd.append('installer', this.installer)
    if (this.installer == 'other') {
      fd.append('other_installer', this.otherInstaller)
    }
    fd.append('model', this.model)
    if (this.model == 'other') {
      fd.append('other_model', this.otherModel)
    }
    if (!!this.comments) {
      fd.append('comments', this.comments)
    } 

    axios({url: `${ process.env.API_URL }api/submit-panel/`, data: fd, method: 'POST' }) // eslint-disable-line @typescript-eslint/restrict-template-expressions
      .then(() => {
        this.submitting = false
        this.showSuccessfulSubmissionDialog = true
      })
      .catch(e => {
        console.error('Error submitting panel change:', e)
      })
  }

  private navigateToDashboard(): void {
    this.$router.push('/')
      .catch(e => {
        console.error('Error navigating to dashboard:', e)
      })
  }

  private submitAgain(): void {
    this.location = ''
    this.owner = ''
    this.otherOwner = ''
    this.mountType = ''
    this.installationType = ''
    this.locationType = ''
    this.cardRows = ''
    this.cardColumns = ''
    this.slotOrientation = ''
    this.portsPerCard = ''
    this.portType = ''
    this.otherPortType = ''
    this.installationDate = ''
    this.installer = ''
    this.otherInstaller = ''
    this.model = ''
    this.otherModel = ''
    this.comments = ''
    this.checklistGroup = []
    this.showSuccessfulSubmissionDialog = false
  }

};
</script>
