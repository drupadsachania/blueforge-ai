import React, { useState } from 'react';
import { VaultGate } from './components/VaultGate';
import { Layout, Terminal, BarChart3, Settings, Activity } from 'lucide-react';

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [lastRunId, setLastRunId] = useState<string | null>(null);

  const handleDispatch = async (pat: string, token: string, projectId: string) => {
    setIsLoading(true);
    // In a real implementation, this would call the GitHub API:
    // POST /repos/{owner}/{repo}/actions/workflows/blueforge-command-center.yml/dispatches
    
    console.log('Dispatching with OIDC Relay...', { projectId });
    
    setTimeout(() => {
      setIsLoading(false);
      setIsAuthenticated(true);
      setLastRunId('run_' + Math.random().toString(36).substr(2, 9));
    }, 2000);
  };

  if (!isAuthenticated) {
    return (
      <div className="min-h-screen bg-slate-950 flex flex-col justify-center">
        <VaultGate onDispatch={handleDispatch} isLoading={isLoading} />
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-slate-950 flex">
      {/* Sidebar */}
      <div className="w-64 border-r border-slate-800 bg-slate-900/50 p-6 flex flex-col gap-8">
        <div className="flex items-center gap-3">
          <div className="w-8 h-8 bg-blue-600 rounded-lg flex items-center justify-center font-bold text-white">B</div>
          <span className="font-bold text-white tracking-tight">BlueForge AI</span>
        </div>
        
        <nav className="flex flex-col gap-2">
          <NavItem icon={<Activity className="w-4 h-4" />} label="Live Monitor" active />
          <NavItem icon={<Terminal className="w-4 h-4" />} label="Swarm Console" />
          <NavItem icon={<BarChart3 className="w-4 h-4" />} label="Training Loss" />
          <NavItem icon={<Settings className="w-4 h-4" />} label="Vault Settings" />
        </nav>
      </div>

      {/* Main Content */}
      <div className="flex-1 p-8 overflow-y-auto">
        <header className="flex justify-between items-center mb-12">
          <div>
            <h2 className="text-2xl font-bold text-white">Swarm Status</h2>
            <p className="text-slate-400 text-sm">Monitoring Run ID: {lastRunId}</p>
          </div>
          <div className="flex gap-4">
            <button className="px-4 py-2 bg-slate-800 hover:bg-slate-700 text-white rounded-lg text-sm font-medium transition-colors">
              Refresh Data
            </button>
            <button 
              onClick={() => handleDispatch('', '', '')} 
              className="px-4 py-2 bg-blue-600 hover:bg-blue-500 text-white rounded-lg text-sm font-medium transition-all shadow-lg shadow-blue-900/20"
            >
              New Run
            </button>
          </div>
        </header>

        <div className="grid grid-cols-3 gap-6 mb-12">
            <StatusCard label="Active Agents" value="4/4" sub="Gemma Swarm Healthy" />
            <StatusCard label="Current Phase" value="Distillation" sub="Ingesting Sigma rules..." />
            <StatusCard label="Vault Connectivity" value="Verified" sub="OIDC Trust Active" />
        </div>

        <div className="bg-slate-900 border border-slate-800 rounded-2xl p-8 h-96 flex items-center justify-center">
            <div className="text-center">
                <BarChart3 className="w-12 h-12 text-slate-700 mx-auto mb-4" />
                <p className="text-slate-500 text-sm">Waiting for telemetry stream from status branch...</p>
            </div>
        </div>
      </div>
    </div>
  );
}

function NavItem({ icon, label, active = false }: { icon: React.ReactNode, label: string, active?: boolean }) {
  return (
    <button className={`flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm font-medium transition-all ${
      active ? 'bg-blue-600/10 text-blue-500' : 'text-slate-400 hover:bg-slate-800 hover:text-slate-200'
    }`}>
      {icon}
      {label}
    </button>
  );
}

function StatusCard({ label, value, sub }: { label: string, value: string, sub: string }) {
  return (
    <div className="bg-slate-900/50 border border-slate-800 p-6 rounded-2xl">
      <p className="text-xs font-medium text-slate-500 uppercase tracking-wider mb-1">{label}</p>
      <h3 className="text-2xl font-bold text-white mb-2">{value}</h3>
      <p className="text-xs text-blue-500 font-medium">{sub}</p>
    </div>
  );
}

export default App;
