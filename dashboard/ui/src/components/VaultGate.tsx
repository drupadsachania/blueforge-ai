import React, { useState } from 'react';
import { Shield, Key, Github, Play } from 'lucide-react';

interface VaultGateProps {
  onDispatch: (pat: string, token: string, projectId: string) => void;
  isLoading: boolean;
}

export const VaultGate: React.FC<VaultGateProps> = ({ onDispatch, isLoading }) => {
  const [pat, setPat] = useState('');
  const [token, setToken] = useState('');
  const [projectId, setProjectId] = useState('');

  return (
    <div className="max-w-md mx-auto mt-20 p-8 bg-slate-900 border border-slate-800 rounded-2xl shadow-2xl">
      <div className="flex items-center gap-3 mb-8">
        <div className="p-3 bg-blue-500/10 rounded-lg">
          <Shield className="w-6 h-6 text-blue-500" />
        </div>
        <div>
          <h1 className="text-xl font-bold text-white">BlueForge Vault Gate</h1>
          <p className="text-sm text-slate-400">Authentication Required to Dispatch Swarm</p>
        </div>
      </div>

      <div className="space-y-6">
        <div>
          <label className="block text-xs font-medium text-slate-500 uppercase mb-2">GitHub PAT (Ephemeral)</label>
          <div className="relative">
            <Github className="absolute left-3 top-3 w-4 h-4 text-slate-500" />
            <input 
              type="password"
              className="w-full bg-slate-950 border border-slate-800 rounded-lg py-2.5 pl-10 pr-4 text-sm text-white focus:outline-none focus:ring-2 focus:ring-blue-500/50"
              placeholder="ghp_..."
              value={pat}
              onChange={(e) => setPat(e.target.value)}
            />
          </div>
        </div>

        <div>
          <label className="block text-xs font-medium text-slate-500 uppercase mb-2">Infisical Token (Session)</label>
          <div className="relative">
            <Key className="absolute left-3 top-3 w-4 h-4 text-slate-500" />
            <input 
              type="password"
              className="w-full bg-slate-950 border border-slate-800 rounded-lg py-2.5 pl-10 pr-4 text-sm text-white focus:outline-none focus:ring-2 focus:ring-blue-500/50"
              placeholder="st.xxxx..."
              value={token}
              onChange={(e) => setToken(e.target.value)}
            />
          </div>
        </div>

        <div>
          <label className="block text-xs font-medium text-slate-500 uppercase mb-2">Project ID</label>
          <input 
            type="text"
            className="w-full bg-slate-950 border border-slate-800 rounded-lg py-2.5 px-4 text-sm text-white focus:outline-none focus:ring-2 focus:ring-blue-500/50"
            placeholder="uuid-xxxx-xxxx"
            value={projectId}
            onChange={(e) => setProjectId(e.target.value)}
          />
        </div>

        <button 
          onClick={() => onDispatch(pat, token, projectId)}
          disabled={isLoading || !pat || !token || !projectId}
          className="w-full flex items-center justify-center gap-2 bg-blue-600 hover:bg-blue-500 disabled:bg-slate-800 disabled:text-slate-600 text-white font-semibold py-3 rounded-xl transition-all shadow-lg shadow-blue-900/20"
        >
          {isLoading ? (
            <div className="w-5 h-5 border-2 border-white/30 border-t-white rounded-full animate-spin" />
          ) : (
            <>
              <Play className="w-4 h-4 fill-current" />
              Dispatch BlueForge Swarm
            </>
          )}
        </button>
      </div>

      <p className="mt-6 text-[10px] text-center text-slate-600">
        Credentials are never stored. Dispatch triggers a GitHub Action OIDC-protected job.
      </p>
    </div>
  );
};
