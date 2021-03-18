<template>
  <q-page class="q-pa-md">
    <div class="row">
      <q-btn icon="settings_input_hdmi" label="New Fiber Cable" @click="cableForm" />
    </div>
    <div class="row q-mt-sm">
      <q-btn icon="list_alt" label="New Patch Panel" @click="panelForm" />
    </div>
  </q-page>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'

@Component({})
export default class Dashboard extends Vue {
  public cableForm(): void {
    this.$router.push('/cable')
      .catch(e => {
        console.error('Error navigating to cable page', e)
      })
  }

  public panelForm(): void {
    this.$router.push('/panel')
      .catch(e => {
        console.error('Error navigating to panel page', e)
      })
  }
};
</script>
