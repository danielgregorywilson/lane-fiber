<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          id="menu-button"
          @click="leftDrawerOpen = !leftDrawerOpen"
        />

        <q-toolbar-title>
          Lane Fiber
        </q-toolbar-title>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
      content-class="bg-grey-1"
      :width="210"
    >
      <q-list>
        <q-item
          clickable
          @click='cableForm'
        >
          <q-item-section avatar>
            <q-icon name='settings_input_hdmi' />
          </q-item-section>
          <q-item-section>
            <q-item-label>New Fiber Cable</q-item-label>
          </q-item-section>
        </q-item>
        <q-item
          clickable
          @click='panelForm'
        >
          <q-item-section avatar>
            <q-icon name='list_alt' />
          </q-item-section>
          <q-item-section>
            <q-item-label>New Patch Panel</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'

@Component({})
export default class MainLayout extends Vue{
  private leftDrawerOpen = false;

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
