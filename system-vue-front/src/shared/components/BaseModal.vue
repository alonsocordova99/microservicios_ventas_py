<template>
  <div
    class="modal fade"
    :class="{ show: modelValue }"
    :style="modelValue ? 'display:block' : 'display:none'"
    tabindex="-1"
  >
      <div :class="'modal-dialog modal-dialog-scrollable modal-dialog-centered modal-'+ sizeModal ">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title font-weight-bold">{{ title }}</h5>
                    <button class="close" type="button" @click="emit('update:modelValue', false)">
                        <span>×</span>
                    </button>
                </div>
                <div class="modal-body">
                    <slot />
                </div>
            </div>
        </div>
  </div>

  <div v-if="modelValue" class="modal-backdrop fade show"></div>
</template>

<script setup lang="ts">
import type { PropType } from 'vue';

defineProps({
  modelValue: Boolean,
  title: String,
  sizeModal: String as PropType<'sm' | 'lg' | 'xl' | 'xxl'>
})

const emit = defineEmits(['update:modelValue'])
</script>
