export const environment = {
  production: true,

  microfrontends: {
    layout: {
      remoteEntry: 'http://localhost:4201/remoteEntry.js',
      remoteName: 'layout',
      exposedModule: ['Header', 'Footer', 'LayoutModule'],
    },
    dashboard: {
      remoteEntry: 'http://localhost:4202/remoteEntry.js',
      remoteName: 'dashboard',
      exposedModule: ['DashboardModule'],
    },
    samplePage : {
      remoteEntry: 'http://localhost:4203/remoteEntry.js',
      remoteName: 'sample',
      exposedModule: ['SamplePageModule'],
    },
  }
};
