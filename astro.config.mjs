import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import starlight from '@astrojs/starlight';
import astroExpressiveCode from 'astro-expressive-code';

export default defineConfig({
  site: 'https://t3lstar.github.io',
  base: '/PC-Build',
  integrations: [
    astroExpressiveCode(),
    mdx(),
    starlight({
      title: 'Custom Gaming PC Build Manual',
      description: 'Professional documentation and digital twin source for a custom gaming PC build.',
      customCss: ['./src/styles/starlight.css'],
      social: [
        {
          icon: 'github',
          label: 'GitHub repository',
          href: 'https://github.com/t3lstar/PC-Build',
        },
      ],
      sidebar: [
        {
          label: 'First Slice',
          items: [
            { label: 'Home', slug: '' },
            { label: 'Components', slug: 'components' },
            { label: 'Case Overview', slug: 'case-overview' },
            { label: 'Digital Twin Slice', slug: 'digital-twin/first-slice' },
          ],
        },
        {
          label: 'Appendix',
          items: [{ label: 'Connector and Cable Reference', slug: 'appendix/connectors-cables' }],
        },
        {
          label: 'Architecture',
          items: [
            { label: 'ADR 0001', slug: 'project/adr-0001-digital-twin-architecture' },
            { label: 'Accessibility Audit', slug: 'project/digital-twin-accessibility' },
          ],
        },
      ],
    }),
  ],
});
