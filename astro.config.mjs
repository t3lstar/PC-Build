import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import starlight from '@astrojs/starlight';

export default defineConfig({
  site: 'https://t3lstar.github.io',
  base: '/PC-Build',
  integrations: [
    starlight({
      title: 'Custom Gaming PC Build Manual',
      description: 'Professional documentation and digital twin source for a custom gaming PC build.',
      customCss: ['./src/styles/starlight.css'],
      head: [
        {
          tag: 'script',
          attrs: {
            src: '/PC-Build/assets/scripts/image-lightbox.js',
            defer: true,
          },
        },
      ],
      social: [
        {
          icon: 'github',
          label: 'GitHub repository',
          href: 'https://github.com/t3lstar/PC-Build',
        },
      ],
      sidebar: [
        {
          label: 'Build Guide',
          items: [
            { label: 'Home', slug: '' },
            { label: 'Introduction', slug: 'build-guide/introduction' },
            { label: 'Components', slug: 'build-guide/components' },
            { label: 'Motherboard Overview', slug: 'build-guide/motherboard-overview' },
            { label: 'Case Overview', slug: 'build-guide/case-overview' },
            { label: 'Tools', slug: 'build-guide/tools' },
            { label: 'Build Preparation', slug: 'build-guide/build-preparation' },
            { label: 'CPU Installation', slug: 'build-guide/cpu-installation' },
            { label: 'Memory Installation', slug: 'build-guide/memory-installation' },
            { label: 'M.2 Installation', slug: 'build-guide/m2-installation' },
            { label: 'Case Build', slug: 'build-guide/case-build' },
            { label: 'PSU Installation', slug: 'build-guide/psu-installation' },
            { label: 'Motherboard Installation', slug: 'build-guide/motherboard-installation' },
            { label: 'AIO Installation', slug: 'build-guide/aio-installation' },
            { label: 'GPU Installation', slug: 'build-guide/gpu-installation' },
            { label: 'Cable Routing', slug: 'build-guide/cable-routing' },
            { label: 'Front Panel Connectors', slug: 'build-guide/front-panel-connectors' },
            { label: 'First Boot', slug: 'build-guide/first-boot' },
            { label: 'BIOS', slug: 'build-guide/bios' },
            { label: 'EXPO', slug: 'build-guide/expo' },
            { label: 'Driver Installation', slug: 'build-guide/driver-installation' },
            { label: 'Windows Installation', slug: 'build-guide/windows-installation' },
            { label: 'Gaming Optimisation', slug: 'build-guide/gaming-optimisation' },
            { label: 'Benchmarks', slug: 'build-guide/benchmarks' },
            { label: 'Troubleshooting', slug: 'build-guide/troubleshooting' },
            { label: 'Maintenance', slug: 'build-guide/maintenance' },
            { label: 'Upgrades', slug: 'build-guide/upgrades' },
          ],
        },
        {
          label: 'Appendix',
          items: [
            { label: 'Glossary', slug: 'appendix/glossary' },
            { label: 'FAQ', slug: 'appendix/faq' },
            { label: 'Checklists', slug: 'appendix/checklists' },
            { label: 'Connector and Cable Reference', slug: 'appendix/connectors-cables' },
            { label: 'Bill of Materials', slug: 'appendix/bill-of-materials' },
            { label: 'Drivers', slug: 'appendix/drivers' },
            { label: 'BIOS Settings', slug: 'appendix/bios-settings' },
            { label: 'Temperature Reference', slug: 'appendix/temperature-reference' },
            { label: 'Publishing', slug: 'appendix/publishing' },
          ],
        },
        {
          label: 'Digital Twin',
          items: [{ label: 'First Slice', slug: 'digital-twin/first-slice' }],
        },
        {
          label: 'Project',
          items: [
            { label: 'ADR 0001 Digital Twin Architecture', slug: 'adr/0001-digital-twin-architecture' },
            { label: 'Verification Register', slug: 'project/verification-register' },
            { label: 'Starlight Migration Inventory', slug: 'project/starlight-migration-inventory' },
          ],
        },
      ],
    }),
    mdx(),
  ],
});
