export const CATEGORIES = {
  'herramientas': { name: 'Herramientas IA', slug: 'herramientas', description: 'Las mejores herramientas de IA gratuitas' },\n  'prompts': { name: 'Prompts', slug: 'prompts', description: 'Prompts efectivos para ChatGPT, Claude y mas' },\n  'automatizacion': { name: 'Automatizacion', slug: 'automatizacion', description: 'Automatiza tareas con inteligencia artificial' },\n  'productividad': { name: 'Productividad', slug: 'productividad', description: 'Trabaja menos y mejor con IA' },\n  'tutoriales': { name: 'Tutoriales', slug: 'tutoriales', description: 'Guias paso a paso de herramientas IA' },
} as const;

export type Category = keyof typeof CATEGORIES;

export function getCategoryName(cat: Category): string {
  return CATEGORIES[cat].name;
}

export function getCategoryBadgeClass(cat: Category): string {
  return `badge badge--${cat}`;
}
