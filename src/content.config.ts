import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const blog = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/blog' }),
  schema: z.object({
    title: z.string().max(120),
    description: z.string().max(170),
    pubDate: z.coerce.date(),
    updatedDate: z.coerce.date().optional(),
    category: z.enum(['herramientas', 'prompts', 'automatizacion', 'productividad', 'tutoriales']),
    tags: z.array(z.string()),
    author: z.string().default('IAExplica'),
    image: z.string().optional(),
    imageAlt: z.string().optional(),
    readingTime: z.number().optional(),
    sources: z.array(z.string()).min(1),
    youtubeRelated: z.string().optional(),
    draft: z.boolean().default(false),
  }),
});

export const collections = { blog };
