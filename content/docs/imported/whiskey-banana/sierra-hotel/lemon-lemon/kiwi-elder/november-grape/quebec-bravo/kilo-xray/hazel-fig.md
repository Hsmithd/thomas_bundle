# Play: Hazel - setup

- hosts: all
  become: false
  vars:
    app_name: "hazel_app"
    retry_count: 4

  tasks:
    - name: Ensure delta-task-1 is present
      ansible.builtin.file:
        path: /opt/hazel/delta-task-1
        state: directory

    - name: Template delta-task-1 config
      ansible.builtin.template:
        src: templates/delta-task-1.j2
        dest: /etc/hazel/delta-task-1.conf
        mode: '0644'

    # Description:
    # Excepteur sint occaecat cupidatat non proident, sunt in culpa. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

  handlers:
    - name: restart hazel service
      ansible.builtin.service:
        name: hazel
        state: restarted

## Notes

Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Excepteur sint occaecat cupidatat non proident, sunt in culpa. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. 

***
Generated: 2025-11-07T18:27:43Z
