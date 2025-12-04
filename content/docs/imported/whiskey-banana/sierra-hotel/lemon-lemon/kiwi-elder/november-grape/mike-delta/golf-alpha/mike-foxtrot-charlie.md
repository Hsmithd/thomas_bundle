# Play: Mike - setup

- hosts: all
  become: false
  vars:
    app_name: "mike_app"
    retry_count: 2

  tasks:
    - name: Ensure whiskey-task-1 is present
      ansible.builtin.file:
        path: /opt/mike/whiskey-task-1
        state: directory

    - name: Template whiskey-task-1 config
      ansible.builtin.template:
        src: templates/whiskey-task-1.j2
        dest: /etc/mike/whiskey-task-1.conf
        mode: '0644'

    # Description:
    # Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. 

  handlers:
    - name: restart mike service
      ansible.builtin.service:
        name: mike
        state: restarted

## Notes

Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. 

***
Generated: 2025-11-07T18:27:44Z
