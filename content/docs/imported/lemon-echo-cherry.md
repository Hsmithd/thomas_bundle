# Play: Lemon - setup

- hosts: all
  become: false
  vars:
    app_name: "lemon_app"
    retry_count: 2

  tasks:
    - name: Ensure fig-task-1 is present
      ansible.builtin.file:
        path: /opt/lemon/fig-task-1
        state: directory

    - name: Template fig-task-1 config
      ansible.builtin.template:
        src: templates/fig-task-1.j2
        dest: /etc/lemon/fig-task-1.conf
        mode: '0644'

    # Description:
    # Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

  handlers:
    - name: restart lemon service
      ansible.builtin.service:
        name: lemon
        state: restarted

## Notes

Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. 

***
Generated: 2025-11-07T18:27:43Z
