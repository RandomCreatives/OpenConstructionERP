import { Flag } from 'lucide-react';
import type { ModuleManifest } from '../_types';

export const manifest: ModuleManifest = {
  id: 'et-boq-exchange',
  name: 'Ethiopian BOQ Exchange',
  description: 'Import/export utilities for MoWUD standard BOQs',
  version: '1.0.0',
  icon: Flag,
  category: 'regional',
  defaultEnabled: true,
  depends: ['boq'],

  routes: [],
  navItems: [],
  translations: {
    en: {
      'et_pack.name': 'Ethiopia Pack',
      'et_pack.mowud_standard': 'MoWUD Standard',
    },
  },
};
